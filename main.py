from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import Qt, QPoint, QBasicTimer, QSize


from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget



class ExampleWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setMinimumSize(QSize(800, 600))
		self.setWindowTitle('Пришельцы')
		central_widget = QWidget(self)
		self.setCentralWidget(central_widget)

		self.alien_unit = []
		self.step_x = 50
		self.step_y = 50
		self.alien_size = 50
		self.alien_unit_img = QtGui.QPixmap('unit1.png')
		self.player = QtWidgets.QLabel(self)
		self.player_img = QtGui.QPixmap('player.png')
		self.player_x = 0

	def squad(self):
		for i in range(10):
			self.alien_unit.append(QtWidgets.QLabel(self))	
			self.alien_unit[i].setPixmap(self.alien_unit_img)
			self.alien_unit[i].setGeometry(QtCore.QRect(self.step_x, 100, self.alien_size, self.alien_size))	
			self.step_x += self.alien_size

	def my_player(self):
		self.player.setPixmap(self.player_img)
		self.player.setGeometry(QtCore.QRect(self.player_x, 300, self.alien_size, self.alien_size))
		

	def keyPressEvent(self, event):
		if event.key() == QtCore.Qt.Key_Q:
			self.player.setGeometry(QtCore.QRect(self.player_x, 300, self.alien_size, self.alien_size))
			self.player_x += 1
			print(self.player_x)
		event.accept()

app = QtWidgets.QApplication(sys.argv)
main_window = ExampleWindow()
main_window.squad()
main_window.my_player()
main_window.show()
sys.exit(app.exec_())

	

	