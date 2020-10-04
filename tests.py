import unittest
from classes import GameBoard
from classes import Color
from classes import Segment
from classes import Box

class TestDotsAndBoxes(unittest.TestCase):

    def test_gameboard_available_squares(self):
        gb = GameBoard(4, 4)
        self.assertEqual(gb.available_squares, 9)

    def test_gameboard_available_squares_rectangle(self):
        gb = GameBoard(8, 10)
        self.assertEqual(gb.available_squares, 63)

    def test_gameboard_too_small(self):
        gb = GameBoard(1, -10)
        self.assertEqual(gb.w, 2)

    def test_gameboard_too_large(self):
        gb = GameBoard(8, 50)
        self.assertEqual(gb.h, 10)

    def test_segment_equals(self):
        p1 = (1, 1)
        p2 = (1, 2)
        s1 = Segment(p1, p2)
        s2 = Segment(p1, p2)
        self.assertTrue(s1.equals(s2))

    def test_segment_equals_unordered(self):
        p1 = (1, 1)
        p2 = (1, 2)
        s1 = Segment(p1, p2)
        s2 = Segment(p2, p1)
        self.assertTrue(s1.equals(s2))

    def test_segment_not_equals(self):
        p1 = (1, 1)
        p2 = (1, 2)
        p3 = (0, 1)
        p4 = (0, 2)
        s1 = Segment(p1, p2)
        s2 = Segment(p3, p4)
        self.assertFalse(s1.equals(s2))

    def test_segment_not_equals_shared(self):
        p1 = (1, 1)
        p2 = (1, 2)
        p3 = (1, 0)
        s1 = Segment(p1, p2)
        s2 = Segment(p3, p2)
        self.assertFalse(s1.equals(s2))

    def test_segment_is_open(self):
        p1 = (1, 1)
        p2 = (1, 2)
        s1 = Segment(p1, p2)
        self.assertTrue(s1.is_open())

    def test_segment_is_open(self):
        p1 = (1, 1)
        p2 = (1, 2)
        s1 = Segment(p1, p2)
        s1.color = Color.RED
        self.assertFalse(s1.is_open())

    def test_box_contains(self):
        p1 = (0, 0)
        p2 = (0, 1)
        p3 = (1, 0)
        p4 = (1, 1)
        s1 = Segment(p1, p3)
        s2 = Segment(p1, p2)
        s3 = Segment(p4, p2)
        s4 = Segment(p4, p3)
        b = Box([s1, s2, s3, s4])
        self.assertTrue(s1 in b)

    def test_box_does_not_contains(self):
        p1 = (0, 0)
        p2 = (0, 1)
        p3 = (1, 0)
        p4 = (1, 1)
        s1 = Segment(p1, p3)
        s2 = Segment(p1, p2)
        s3 = Segment(p4, p2)
        s4 = Segment(p4, p3)
        b = Box([s1, s2, s3, s4])

        p5 = (2, 1)
        s5 = Segment(p4, p5)
        self.assertFalse(s5 in b)

    def test_box_complete(self):
        p1 = (0, 0)
        p2 = (0, 1)
        p3 = (1, 0)
        p4 = (1, 1)
        s1 = Segment(p1, p3)
        s1.color = Color.RED
        s2 = Segment(p1, p2)
        s2.color = Color.BLUE
        s3 = Segment(p4, p2)
        s3.color = Color.RED
        s4 = Segment(p4, p3)
        s4.color = Color.BLUE
        b = Box([s1, s2, s3, s4])

        b.add_completed_segment(s1)
        b.add_completed_segment(s2)
        b.add_completed_segment(s3)
        b.add_completed_segment(s4)
        self.assertTrue(b.is_complete())

    def test_box_not_complete(self):
        p1 = (0, 0)
        p2 = (0, 1)
        p3 = (1, 0)
        p4 = (1, 1)
        s1 = Segment(p1, p3)
        s1.color = Color.RED
        s2 = Segment(p1, p2)
        s2.color = Color.BLUE
        s3 = Segment(p4, p2)
        s3.color = Color.RED
        s4 = Segment(p4, p3)
        s4.color = Color.BLUE
        b = Box([s1, s2, s3, s4])

        b.add_completed_segment(s1)
        b.add_completed_segment(s4)
        self.assertFalse(b.is_complete())

    def test_box_owner(self):
        p1 = (0, 0)
        p2 = (0, 1)
        p3 = (1, 0)
        p4 = (1, 1)
        s1 = Segment(p1, p3)
        s1.color = Color.RED
        s2 = Segment(p1, p2)
        s2.color = Color.BLUE
        s3 = Segment(p4, p2)
        s3.color = Color.RED
        s4 = Segment(p4, p3)
        s4.color = Color.BLUE
        b = Box([s1, s2, s3, s4])

        b.add_completed_segment(s1)
        b.add_completed_segment(s2)
        b.add_completed_segment(s3)
        b.add_completed_segment(s4)
        self.assertTrue(b.owner == Color.BLUE)

if __name__ == '__main__':
    unittest.main()