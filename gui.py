# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.main_widget = QtWidgets.QWidget(MainWindow)
        self.main_widget.setMinimumSize(QtCore.QSize(800, 600))
        self.main_widget.setMaximumSize(QtCore.QSize(800, 600))
        self.main_widget.setObjectName("main_widget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.main_widget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 790, 590))
        self.stackedWidget.setObjectName("stackedWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.home)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 781, 581))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.home_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.home_layout.setContentsMargins(0, 0, 0, 0)
        self.home_layout.setObjectName("home_layout")
        self.title = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.title.setMinimumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.home_layout.addWidget(self.title, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.home_layout.addItem(spacerItem)
        self.start_game_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.start_game_btn.setMinimumSize(QtCore.QSize(250, 50))
        self.start_game_btn.setMaximumSize(QtCore.QSize(250, 50))
        self.start_game_btn.setObjectName("start_game_btn")
        self.home_layout.addWidget(self.start_game_btn, 0, QtCore.Qt.AlignHCenter)
        self.join_game_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.join_game_btn.setMinimumSize(QtCore.QSize(250, 50))
        self.join_game_btn.setMaximumSize(QtCore.QSize(250, 50))
        self.join_game_btn.setObjectName("join_game_btn")
        self.home_layout.addWidget(self.join_game_btn, 0, QtCore.Qt.AlignHCenter)
        self.settings_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.settings_btn.setMinimumSize(QtCore.QSize(250, 50))
        self.settings_btn.setMaximumSize(QtCore.QSize(250, 50))
        self.settings_btn.setObjectName("settings_btn")
        self.home_layout.addWidget(self.settings_btn, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.home_layout.addItem(spacerItem1)
        self.stackedWidget.addWidget(self.home)
        self.game = QtWidgets.QWidget()
        self.game.setObjectName("game")
        self.stackedWidget.addWidget(self.game)
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.settings)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 781, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.gameboard_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.gameboard_layout.setContentsMargins(0, 0, 0, 0)
        self.gameboard_layout.setObjectName("gameboard_layout")
        self.gameboard_group_box = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.gameboard_group_box.setObjectName("gameboard_group_box")
        self.formLayoutWidget = QtWidgets.QWidget(self.gameboard_group_box)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 761, 501))
        self.formLayoutWidget.setMinimumSize(QtCore.QSize(50, 0))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.gameboard_grid_layout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.gameboard_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.gameboard_grid_layout.setObjectName("gameboard_grid_layout")
        self.width_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.width_label.setMinimumSize(QtCore.QSize(50, 0))
        self.width_label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.width_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.width_label.setObjectName("width_label")
        self.gameboard_grid_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.width_label)
        self.width_spin_box = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.width_spin_box.setMinimumSize(QtCore.QSize(35, 0))
        self.width_spin_box.setMaximumSize(QtCore.QSize(35, 16777215))
        self.width_spin_box.setMinimum(2)
        self.width_spin_box.setMaximum(10)
        self.width_spin_box.setProperty("value", 6)
        self.width_spin_box.setObjectName("width_spin_box")
        self.gameboard_grid_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.width_spin_box)
        self.height_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.height_label.setMinimumSize(QtCore.QSize(50, 0))
        self.height_label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.height_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.height_label.setObjectName("height_label")
        self.gameboard_grid_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.height_label)
        self.height_spin_box = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.height_spin_box.setMinimumSize(QtCore.QSize(35, 0))
        self.height_spin_box.setMaximumSize(QtCore.QSize(35, 16777215))
        self.height_spin_box.setMinimum(2)
        self.height_spin_box.setMaximum(10)
        self.height_spin_box.setProperty("value", 6)
        self.height_spin_box.setObjectName("height_spin_box")
        self.gameboard_grid_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.height_spin_box)
        self.gameboard_layout.addWidget(self.gameboard_group_box)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.settings)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 539, 781, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.settings_navigation_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.settings_navigation_layout.setContentsMargins(0, 0, 0, 0)
        self.settings_navigation_layout.setObjectName("settings_navigation_layout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.settings_navigation_layout.addItem(spacerItem2)
        self.ok_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ok_btn.setMinimumSize(QtCore.QSize(100, 0))
        self.ok_btn.setObjectName("ok_btn")
        self.settings_navigation_layout.addWidget(self.ok_btn)
        self.cancel_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancel_btn.setMinimumSize(QtCore.QSize(100, 0))
        self.cancel_btn.setObjectName("cancel_btn")
        self.settings_navigation_layout.addWidget(self.cancel_btn)
        self.stackedWidget.addWidget(self.settings)
        self.game_over = QtWidgets.QWidget()
        self.game_over.setObjectName("game_over")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.game_over)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 781, 581))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.game_over_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.game_over_label.setMinimumSize(QtCore.QSize(0, 150))
        self.game_over_label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(48)
        font.setItalic(False)
        font.setUnderline(True)
        self.game_over_label.setFont(font)
        self.game_over_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.game_over_label.setObjectName("game_over_label")
        self.verticalLayout.addWidget(self.game_over_label)
        self.winner_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.winner_label.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.winner_label.setFont(font)
        self.winner_label.setAlignment(QtCore.Qt.AlignCenter)
        self.winner_label.setObjectName("winner_label")
        self.verticalLayout.addWidget(self.winner_label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.losing_player_name_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.losing_player_name_label.setMinimumSize(QtCore.QSize(0, 75))
        self.losing_player_name_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.losing_player_name_label.setObjectName("losing_player_name_label")
        self.gridLayout.addWidget(self.losing_player_name_label, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        self.winning_player_name_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.winning_player_name_label.setMinimumSize(QtCore.QSize(0, 75))
        self.winning_player_name_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.winning_player_name_label.setObjectName("winning_player_name_label")
        self.gridLayout.addWidget(self.winning_player_name_label, 0, 0, 1, 1)
        self.losing_player_score_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.losing_player_score_label.setMinimumSize(QtCore.QSize(0, 75))
        self.losing_player_score_label.setObjectName("losing_player_score_label")
        self.gridLayout.addWidget(self.losing_player_score_label, 1, 1, 1, 1)
        self.winning_player_score_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.winning_player_score_label.setMinimumSize(QtCore.QSize(0, 75))
        self.winning_player_score_label.setObjectName("winning_player_score_label")
        self.gridLayout.addWidget(self.winning_player_score_label, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.return_home_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.return_home_btn.setObjectName("return_home_btn")
        self.horizontalLayout.addWidget(self.return_home_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.stackedWidget.addWidget(self.game_over)
        MainWindow.setCentralWidget(self.main_widget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Dots N\' Boxes"))
        self.start_game_btn.setText(_translate("MainWindow", "Start Game"))
        self.join_game_btn.setText(_translate("MainWindow", "Join Game"))
        self.settings_btn.setText(_translate("MainWindow", "Settings"))
        self.gameboard_group_box.setTitle(_translate("MainWindow", "GameBoard Settings"))
        self.width_label.setText(_translate("MainWindow", "Width:"))
        self.height_label.setText(_translate("MainWindow", "Height:"))
        self.ok_btn.setText(_translate("MainWindow", "OK"))
        self.cancel_btn.setText(_translate("MainWindow", "Cancel"))
        self.game_over_label.setText(_translate("MainWindow", "GAME OVER"))
        self.winner_label.setText(_translate("MainWindow", "{winner} Wins!"))
        self.losing_player_name_label.setText(_translate("MainWindow", "{player}:"))
        self.winning_player_name_label.setText(_translate("MainWindow", "{player}:"))
        self.losing_player_score_label.setText(_translate("MainWindow", "{score}"))
        self.winning_player_score_label.setText(_translate("MainWindow", "{score}"))
        self.return_home_btn.setText(_translate("MainWindow", "OK"))
