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
		self.alien_timer = QBasicTimer()

		self.alien_unit = []
		self.alien_unit_x = []
		self.alien_unit_y = []
		for i in range(18):
			self.alien_unit.append(QtWidgets.QLabel(self))	
			self.alien_unit_x.append(QtWidgets.QLabel(self))	
			self.alien_unit_y.append(QtWidgets.QLabel(self))	
		self.alien_size_x, self.alien_size_y = 68, 55
		self.alien = QtGui.QPixmap('7471.png')
		self.alien_green_img = self.alien.copy(104, 0, self.alien_size_x, self.alien_size_y)
		self.alien_blue_img = self.alien.copy(257, 0, self.alien_size_x, self.alien_size_y)
		self.step_x, self.step_y = 10, 50
		self.alien_speed = 10
		self.player = QtWidgets.QLabel(self)
		self.player_img = QtGui.QPixmap('player.png')
		self.player_x, self.player_y = 400, 540
		self.sd = QtWidgets.QLabel(self)
		self.sd_img = QtGui.QPixmap('sd.png')
		self.sd_img = self.sd_img.scaled(30, 30, Qt.KeepAspectRatio, Qt.FastTransformation)
		self.sd_x, self.sd_y = self.player_x, self.player_y
		self.my_sd = False

	def my_player(self):
		self.player.setPixmap(self.player_img)
		self.player.setGeometry(QtCore.QRect(self.player_x, self.player_y, 70, 58))	
		self.time.start(50, self)	

	def keyPressEvent(self, event):		
		if event.key() == QtCore.Qt.Key_D and self.player_x <= 800-100:
			self.player_x += 10

		if event.key() == QtCore.Qt.Key_A and self.player_x >= 0+50:
			self.player_x -= 10
		if event.key() == QtCore.Qt.Key_S:
			self.my_sd = True

		self.player.setGeometry(QtCore.QRect(self.player_x, self.player_y, 70, 58))					
		event.accept()

	def timerEvent(self, e):
		t = 0
		n = 0

		'''создание пришельцев'''
		for i in range(18): 			
			self.alien_unit[i].setPixmap(self.alien_green_img)
			self.alien_unit[i].setGeometry(QtCore.QRect(self.step_x+t, self.step_y+n, self.alien_size_x, self.alien_size_y))
			self.alien_unit_x[i] = self.step_x+t
			self.alien_unit_y[i] = self.step_y+n
			t += 68 + 30
			if t >= 508: 
				t = 0
				n += 55
			if self.sd_x <= self.alien_unit_x[i] + self.alien_size_x and \
				self.sd_x + 30 >= self.alien_unit_x[i] and \
				self.sd_y <= self.alien_unit_y[i] + self.alien_size_y:
				self.alien_unit[i].setPixmap(self.alien_blue_img)
		'''движение пришельцев'''		
		#self.step_x += self.alien_speed		
		if self.step_x >= 245 or self.step_x <= 0: 
			self.step_y += 10
			self.alien_speed = -self.alien_speed

		'''движение sd'''
		if self.sd_y > 0 and self.my_sd == True:
			self.sd.setPixmap(self.sd_img)
			self.sd.setGeometry(QtCore.QRect(self.sd_x+10, self.sd_y-20, 30, 30))	
			self.sd_y -= 10	
			#print(self.sd_y)	
		else:
			self.my_sd = False
			self.sd_x = self.player_x
			self.sd_y = self.player_y

		print(self.alien_unit_x[0])

app = QtWidgets.QApplication(sys.argv)
main_window = ExampleWindow()

main_window.my_player()
main_window.show()	


sys.exit(app.exec_())
