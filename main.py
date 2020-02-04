from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import QTimer


x = 1
y = 1
a = 10
def window():
	app = QtWidgets.QApplication(sys.argv)
	main_window = QtWidgets.QWidget()	
	main_window.setWindowTitle('MY GAME')
	main_window.setGeometry(700, 300, 300, 200)

	global x
	def move():

		global x, y, a
		x += a
		unit1.move(x,y)	
		txt = (str(x) + '/' + str(y))
		button.setText(txt)
		if x >= 200 or x <= 1:
			a = -a
			y += 10	
			

	button = QtWidgets.QPushButton(main_window)
	unit1 = QtWidgets.QLabel(main_window)
	button.setGeometry(QtCore.QRect(100, 100, 40, 30))
	button.clicked.connect(move)
	unit1.setPixmap(QtGui.QPixmap('unit1.png'))


	main_window.show()
	sys.exit(app.exec_())

window()	

	