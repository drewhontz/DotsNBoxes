from collections import defaultdict
from enum import Enum
from itertools import product
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPen, QPainter, QBrush
from PyQt5.QtWidgets import QMainWindow, QLabel
from gui import Ui_MainWindow
import logging

logger = logging.getLogger('DotsNBoxes')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


class Color(Enum):
    RED = 0
    BLUE = 1


class State(Enum):
    IN_PROGRESS = 0
    COMPLETE = 1


class Orientation(Enum):
    HORIZONTAL = 0
    VERTICAL = 1


class Segment:
    """
    This class represents a line segment between two points on the grid
    It maintains a state of which player has claimed it (via Color) and where it is located
    It can return if it is occupied and compare itself to another segment
    """
    def __init__(self, o, e):
        coords = [o, e]
        coords.sort()
        self.origin = coords[0]
        self.end = coords[1]
        self.color = None
        if self.origin[0] == self.end[0]:
            self.orientation = Orientation.VERTICAL
        else:
            self.orientation = Orientation.HORIZONTAL

    def equals(self, segment):
        """
        Compares segments to determine if they are the same

        :param segment:
        :return: boolean
        """
        return self.origin == segment.origin and self.end == segment.end

    def is_open(self):
        """
        Returns whether or not this segment is playable/claimed

        :return: boolean
        """
        return self.color is None


class Box:
    """
    This class represents a box formed by 4 segments.
    It is responsible for returning whether or not it has been completed by a segment being filled
    It can return whether or not it contains a segment, and whether or not it is completed.
    """
    def __init__(self, segment_list):
        self.segments = segment_list
        self.segments_completed = []
        self.owner = None

    def __contains__(self, segment):
        """
        Checks if a box contains a given segment
        :param segment:
        :return: boolean
        """
        for s in self.segments:
            if s.equals(segment):
                return True
        return False

    def is_complete(self):
        """
        Checks if 4 segments have been completed
        :return:
        """
        return len(self.segments_completed) == 4

    def add_completed_segment(self, segment):
        """
        Adds a segment to the list of completed segments
        Sets the owner property if this is the 4th segment

        :param segment:
        :return: void
        """
        if segment.is_open():
            raise ValueError('Segment is not complete and cannot be added to box.')
        else:
            if segment not in self.segments_completed:
                self.segments_completed.append(segment)
                if self.is_complete():
                    self.owner = segment.color

    def get_coords(self):
        coords = [(s.origin, s.end) for s in self.segments]
        coords.sort()
        return coords


class GameState:
    """
    Maintains the scores and whether or not the game has ended.
    """
    def __init__(self, box_count):
        self.score = {
            Color.RED: 0,
            Color.BLUE: 0
        }
        self.state = State.IN_PROGRESS
        self.boxes_remaining = box_count
        self.player_turn = Color.RED

    def update_score(self, color):
        self.score[color] += 1
        self.boxes_remaining -= 1
        logger.info(f'{color} has scored a point!\nBoxes remaining: {self.boxes_remaining}')
        if self.boxes_remaining == 0:
            self.state = State.COMPLETE
            logger.info(f'Game has ended.\nHere is your score:\n\tRed: {self.score[Color.RED]}\n\tBlue: '
                        f'{self.score[Color.BLUE]}')

    def end_turn(self, turn_ended):
        if turn_ended:
            if self.player_turn == Color.RED:
                self.player_turn = Color.BLUE
                logger.info(f'Red\'s turn has ended. Show me what you got Blue!')
            elif self.player_turn == Color.BLUE:
                self.player_turn = Color.RED
                logger.info(f'Blue\'s turn has ended. Show me what you got Red!')
        elif self.state != State.COMPLETE:
            logger.info(f'It is still {self.player_turn}\'s turn')


class GameBoard:
    """
    This class represents the gameboard and it is responsible for initializing all game variables and drawing segments.
    """
    MIN_SIZE = 2
    MAX_SIZE = 10

    def __init__(self, width, height):
        """

        :param width:
        :param height:
        """
        self.w = self.set_dimension(width)
        self.h = self.set_dimension(height)
        self.available_squares = (self.w - 1) * (self.h - 1)
        # set all the dot coordinates
        x_axis = [_ for _ in range(self.w)]
        y_axis = [_ for _ in range(self.h)]
        self.dot_coordinates = []
        for _ in product(x_axis, y_axis):
            self.dot_coordinates.append(_)
        self.segments = self.create_segments()
        self.boxes = self.create_boxes()
        self.completed_boxes = []
        box_count = (self.w - 1) * (self.h - 1)
        self.state = GameState(box_count)

    @staticmethod
    def set_dimension(x):
        """
        Accepts an integer as a dimension for either the gameboards width or height.
        If x is outside the bounds of the class' min or max size variable, the min or max dimension will be returned.

        Ex: Gameboard(0, 10) with a min_size 2 and max_size 8 would return a 2 x 8 Gameboard.
        :param x:
        :return:
        """
        if x < GameBoard.MIN_SIZE:
            return GameBoard.MIN_SIZE
        elif x > GameBoard.MAX_SIZE:
            return GameBoard.MAX_SIZE
        else:
            return x

    def create_segments(self):
        """
        Sets the gameboard's segment objects from the list of dot coordinates

        :return:
        """
        segments = []
        for coord in self.dot_coordinates:
            if coord[0] + 1 < self.w:
                right = (coord[0] + 1, coord[1])
                s = Segment(coord, right)
                segments.append(s)
            if coord[1] + 1 < self.h:
                above = (coord[0], coord[1] + 1)
                s = Segment(coord, above)
                segments.append(s)
        return segments

    def create_boxes(self):
        """
        Sets the gameboards boxes from the segment list
        """
        boxes = defaultdict(list)
        horizontal_segments = [segment for segment in self.segments if segment.orientation == Orientation.HORIZONTAL]
        vertical_segments = [segment for segment in self.segments if segment.orientation == Orientation.VERTICAL]

        for segment in horizontal_segments:
            # if the cursor segment is not in the top of the gameboard, start building
            if segment.origin[1] != self.h - 1:
                box_under_construction = [segment]
                # add y + 1 to the origin and end of the cursor segment to find the left and right walls
                left_wall = Segment(segment.origin, (segment.origin[0], segment.origin[1] + 1))
                right_wall = Segment(segment.end, (segment.end[0], segment.end[1] + 1))
                # look for a match for the left and right walls and add to the construction list
                for vertical_segment in vertical_segments:
                    if vertical_segment.equals(left_wall) or vertical_segment.equals(right_wall):
                        box_under_construction.append(vertical_segment)
                # finally repeat the process for the top wall, adding y + 1 to origin and end
                upper_wall = Segment((segment.origin[0], segment.origin[1] + 1), (segment.end[0], segment.end[1] + 1))
                for horizontal_segment in horizontal_segments:
                    if horizontal_segment.equals(upper_wall):
                        box_under_construction.append(horizontal_segment)
                # build the box from the list of segments
                box = Box(box_under_construction)
                # for each segment add the newly constructed box object under the segment key
                for key in box_under_construction:
                    boxes[key].append(box)
        return boxes

    def draw_segment(self, color, segment):
        """
        This function will accept a color and a segment and sets the segment color to that which belongs to the player
        who clicked this segment.

        When the segment color has been set, the gameboard will check all boxes that contain this segment.
        If the box is completed, the gameboard delegates to the state object to update the score and that the turn has
        not ended.

        :param color:
        :param segment:
        :return:
        """
        turn_over = True
        # get the segment that was clicked
        for cursor in self.segments:
            if segment.equals(cursor) and segment.is_open():
                # set its color property
                cursor.color = color
                for box in self.boxes[cursor]:
                    # add this as a completed segment to the box containing the segment
                    box.add_completed_segment(cursor)
                    if box.is_complete():
                        self.completed_boxes.append(box)
                        # update the score if the box is completed
                        self.state.update_score(color)
                        turn_over = False
        self.state.end_turn(turn_over)


class GameWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
        self.wire_up_buttons()

    def wire_up_buttons(self):
        self.ui.start_game_btn.clicked.connect(lambda x: self.start_game())
        self.ui.settings_btn.clicked.connect(lambda x: self.change_page(self.ui.settings))
        self.ui.ok_btn.clicked.connect(lambda x: self.change_page(self.ui.home))
        self.ui.cancel_btn.clicked.connect(lambda x: self.change_page(self.ui.home))
        self.ui.return_home_btn.clicked.connect(lambda x: self.change_page(self.ui.home))

    def change_page(self, page_name):
        self.ui.stackedWidget.setCurrentWidget(page_name)

    def start_game(self):
        self.ui.game = GameWidget(
            self
            , self.ui.width_spin_box.value()
            , self.ui.height_spin_box.value()
            , self.width()
            , self.height()
            , 5
            , 100
        )
        self.ui.stackedWidget.addWidget(self.ui.game)
        self.change_page(self.ui.game)
        if self.ui.game.game_board.state == State.COMPLETE:
            logger.info("game over witches")


class GameWidget(QtWidgets.QWidget):
    def __init__(self, game_window, game_width, game_height, window_width, window_height, dot_radius, padding, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setObjectName("game")
        self.game_window = game_window
        self.game_width = game_width
        self.game_height = game_height
        self.window_width = window_width
        self.window_height = window_height
        self.dot_radius = dot_radius
        self.padding = padding
        self.game_board = GameBoard(self.game_width, self.game_height)
        for segment in self.game_board.segments:
            # Draw segment labels on the board
            x, y = self.scale_coord(segment.origin)
            if segment.orientation == Orientation.HORIZONTAL:
                w = self.get_segment_width()
                h = 2 * self.dot_radius
                x += self.dot_radius
            elif segment.orientation == Orientation.VERTICAL:
                w = 2 * self.dot_radius
                h = self.get_segment_height()
                y += self.dot_radius
            SegmentWidget(self, segment, x, y, w, h)

    def paintEvent(self, event):
        # draw the dots and segments based off the current gameboard width
        painter = QPainter(self)
        pen = QPen(QtCore.Qt.black, 5)
        painter.setPen(pen)
        brush = QBrush(QtCore.Qt.black, QtCore.Qt.SolidPattern)
        painter.setBrush(brush)

        # drawing dots on board
        for pt in self.game_board.dot_coordinates:
            x, y = self.scale_coord(pt)
            logger.debug(f"Painting dot at {x}, {y}")
            painter.drawEllipse(x, y, self.dot_radius, self.dot_radius)

        for box in self.game_board.completed_boxes:
            box_origin = box.get_coords()[0][0]
            x, y = self.scale_coord(box_origin)
            w = self.get_segment_width()
            h = self.get_segment_height()
            logger.debug(f"Painting rectancle at {x}, {y}, {w}, {h}")
            if box.owner == Color.RED:
                painter.setBrush(QBrush(QtCore.Qt.red))
            elif box.owner == Color.BLUE:
                painter.setBrush(QBrush(QtCore.Qt.blue))
            painter.drawRect(x, y, w, h)

        if self.game_board.state.state == State.COMPLETE:
            logger.info('Changing page to game over screen')
            if self.game_board.state.score[Color.RED] > self.game_board.state.score[Color.BLUE]:
                winner = 'RED'
                winning_score = str(self.game_board.state.score[Color.RED])
                loser = 'BLUE'
                losing_score = str(self.game_board.state.score[Color.BLUE])
            elif self.game_board.state.score[Color.RED] < self.game_board.state.score[Color.BLUE]:
                winner = 'BLUE'
                winning_score = str(self.game_board.state.score[Color.BLUE])
                loser = 'RED'
                losing_score = str(self.game_board.state.score[Color.RED])
            else:
                winner = 'RED'
                winning_score = str(self.game_board.state.score[Color.RED])
                loser = 'BLUE'
                losing_score = str(self.game_board.state.score[Color.BLUE])

            winner_label_text = self.game_window.ui.winner_label.text().format(winner=winner)
            self.game_window.ui.winner_label.setText(winner_label_text)
            winner_player_label_text = self.game_window.ui.winning_player_name_label.text()\
                .format(player=winner)
            self.game_window.ui.winning_player_name_label.setText(winner_player_label_text)
            winning_player_score_label_text = self.game_window.ui.winning_player_score_label.text()\
                .format(score=winning_score)
            self.game_window.ui.winning_player_score_label.setText(winning_player_score_label_text)
            losing_player_label_text = self.game_window.ui.losing_player_name_label.text()\
                .format(player=loser)
            self.game_window.ui.losing_player_name_label.setText(losing_player_label_text)
            losing_player_score_label_text = self.game_window.ui.losing_player_score_label.text()\
                .format(score=losing_score)
            self.game_window.ui.losing_player_score_label.setText(losing_player_score_label_text)
            self.game_window.change_page(self.game_window.ui.game_over)


    def scale_coord(self, coord):
        """
        Multiplies the x and y coordinate by the size of the gameboard & padding
        :param coord:
        :return:
        """
        x = coord[0]
        y = coord[1]
        x1 = (x * self.get_segment_width()) + self.padding
        y1 = (y * self.get_segment_height()) + self.padding
        return x1, y1

    def get_segment_width(self):
        return ((self.window_width - self.padding) / self.game_width)

    def get_segment_height(self):
        return ((self.window_height - self.padding) / self.game_height)


class SegmentWidget(QLabel):
    def __init__(self, game_widget, segment, x, y, w, h, *args, **kwargs):
        super().__init__(game_widget, *args, **kwargs)
        self.game_widget = game_widget
        self.game_board = game_widget.game_board
        self.segment = segment
        self.setGeometry(x, y, w, h)
        self.setStyleSheet("border: 1px dotted black;")
        self.mousePressEvent = self.clicked

    def clicked(self, event):
        logger.info(str(self.game_board.state.player_turn) + " clicked a segment.")
        if self.game_board.state.player_turn == Color.RED:
            color = 'red'
        elif self.game_board.state.player_turn == Color.BLUE:
            color = 'blue'
        self.setStyleSheet(f"background-color: {color};")
        self.game_board.draw_segment(self.game_board.state.player_turn, self.segment)
        self.game_widget.update()
