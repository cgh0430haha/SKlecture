import sys
from os import listdir

from PyQt4 import QtCore, QtGui

from PyQt4.QtGui import *
#from PyQt4.QtCore import *
#import pictureflow
from pictureflow import *


import sip
print(sip, sip.SIP_VERSION_STR)


class PictureFlow1(PictureFlow): #QtGui.QWidget
	def __init__(self, parent=None):
		super(PictureFlow, self).__init__(parent)
		#self.itemAt=(0,0)
		#self.ui.setupUi(self)



#	def  keyPressEvent(self):
#		print("d")

	#def  addSlide(self):
		#super.addSlide(self)
		#super.addSlide()

	def mouseReleaseEvent(self, event):
		"""
		mouse button release event
		"""
		button = event.button()
		# select an item on which we clicked
		a=event.x()
		item=event.y()
		#item = self.itemAt(event.x(), event.y())
		if item:
			#self.setCurrentItem(item)
			if button == 1:
				print self.centerIndex()
				print 'SIMPLE LEFT CLICK'


app = QApplication(sys.argv)

w = PictureFlow1()
#w = PictureFlow1(w1)


images = listdir('/home/geunho/caffe_SSDH/examples/SSDH/')
for i in images:
	if i.endswith('jpg'):
		w.addSlide(QPixmap('/home/geunho/caffe_SSDH/examples/SSDH/%s' % i))

idx=w.centerIndex()
print(idx)

w.show()

sys.exit(app.exec_())

a =1
b =1


