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
		self.time = QBasicTimer()
		
		self.alien_x = []
		self.alien_y = []
		self.alien_hitbox = []
		self.alien_unit = []
		self.step_x = 100
		self.step_y = 100
		self.alien_size_x = 68
		self.alien_size_y = 55
		self.alien_unit_img = QtGui.QPixmap('unit1.png')
		self.sd_img = QtGui.QPixmap('sd.png')
		self.sd_img = self.sd_img.scaled(30, 30, Qt.KeepAspectRatio, Qt.FastTransformation)
		self.alien = QtGui.QPixmap('7471.png')		
		self.player = QtWidgets.QLabel(self)
		self.player_img = QtGui.QPixmap('player.png')
		self.alien_green_img = self.alien.copy(100, 0, 70, 60)
		self.alien_yello_img = self.alien.copy(180, 0, 70, 60)
		self.alien_blue_img = self.alien.copy(257, 0, self.alien_size_x, self.alien_size_y)
		self.player_x = 400
		self.player_y = 530
		self.sd_y = self.player_y
		self.sd_x = self.player_x
		self.player.setPixmap(self.player_img)
		self.player.setGeometry(QtCore.QRect(self.player_x, self.player_y, 70, 58))

		self.sd = QtWidgets.QLabel(self)
		self.sd.setPixmap(self.sd_img)

			

	def paintEvent (self, e):
		#painter = QtGui.QPainter(self)
		#painter.drawPixmap(self.player_x, 3, self.tarelko, 100, 0, 69, 58)
		#painter.begin(self)
		pass
		#painter.end()


	def squad(self):
		for i in range(6):
			''' создаем пришельцев, их цвета и формы, их местоположение в пространстве'''
			self.alien_unit.append(QtWidgets.QLabel(self))	
			self.alien_unit[i].setPixmap(self.alien_blue_img)
			self.alien_unit[i].setGeometry(QtCore.QRect(self.step_x, self.step_y, self.alien_size_x, self.alien_size_y))	
			self.alien_hitbox.append(QtWidgets.QPushButton(self))
			self.alien_hitbox[i].setGeometry(QtCore.QRect(self.step_x, self.step_y, self.alien_size_x, self.alien_size_y))
			self.alien_hitbox[i].setStyleSheet('QPushButton {background-color: rgba(10,10,10,10); border-style: solid; border-width: 1px; border-color: gray; color: black; }')
			self.alien_x.append(self.step_x)
			self.step_x += self.alien_size_x+30


	def my_player(self):
		#self.player.setPixmap(self.player_img2)
		#self.player.setGeometry(QtCore.QRect(self.player_x, self.player_y, 70, 58))
		pass

	def keyPressEvent(self, event):		
		if event.key() == QtCore.Qt.Key_D and self.player_x <= 800-100:
			self.player_x += 10
		if event.key() == QtCore.Qt.Key_A and self.player_x >= 0+50:
			self.player_x -= 10
		if event.key() == QtCore.Qt.Key_S:
			if self.time.isActive():
				pass
			else:	
				self.sd_y = self.player_y
				self.sd_x = self.player_x
				self.time.start(10, self)			
		self.player.setGeometry(QtCore.QRect(self.player_x, self.player_y, 70, 58))
		event.accept()

	def sd_event(self):
		pass

	def timerEvent(self, e):
		if self.sd_y > 0:
			self.sd_y -= 1		
			self.sd.setGeometry(QtCore.QRect(self.sd_x+10, self.sd_y-20, 30, 30))	
			for i in range(6):
				
				if self.sd_y == self.step_y + self.alien_size_y and self.sd_x + 33 >= self.alien_x[i] and self.sd_x + 17 <= self.alien_x[i] + self.alien_size_x:
					print(self.alien_x[i])

	
		else:
			self.time.stop()	

		self.repaint()




app = QtWidgets.QApplication(sys.argv)
main_window = ExampleWindow()

main_window.squad()
main_window.show()	


sys.exit(app.exec_())

	

	