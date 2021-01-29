import sys, time
from PyQt5.QtWidgets import QApplication, QMainWindow

import GUI

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ui = GUI.GUI()
	ui.show()
	#time.sleep(5)
	#for i in range(10):
	#	ui.road.append([i, 0])
	#ui.update()
	sys.exit(app.exec_())
	