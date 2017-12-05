# -*- coding: utf-8 -*-
# coding: cp949



import sys

from PyQt4 import QtCore, QtGui
from httpWidget import Ui_HttpWidget
from os import listdir
from pictureflow import *
import pandas as pd
import extract_similarity as recommender
import extract_tag
import numpy as np
import matplotlib.pyplot as plt

class PictureFlow1(PictureFlow): #QtGui.QWidget
	def __init__(self, parent=None):
		super(PictureFlow, self).__init__(parent)

#		self.images = listdir('/home/geunho/caffe_SSDH/examples/SSDH/crop_temp/')
		self.center=0
#		self.imgss
		self.tagss, self.imgss = TAGS, IMGS
		self.rank = np.zeros(len(self.tagss))



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
				IDX = self.centerIndex()
				#s='/home/geunho/caffe_SSDH/examples/SSDH/crop_temp/'+self.images[IDX]

				print self.centerIndex()
				self.center = self.centerIndex()


				ss=IMGS[self.rank[self.center]]
				df = pd.DataFrame([ss])
				df.to_clipboard(index=False, header=False)
				print (ss)



class httpWidget(QtGui.QWidget):
	def __init__(self, parent=None):
		super(httpWidget, self).__init__(parent)
		self.ui = Ui_HttpWidget()
		self.ui.setupUi(self)
		
		# set margins
		l = self.layout()
		l.setMargin(0)
		self.ui.horizontalLayout.setMargin(5)
		
		# set the default
		#url = 'http://localhost:8080'
		url = 'http://www.naver.com'
		#url = 'http://www.facebook.com'
		self.ui.url.setText(url)


		# load page
		self.ui.webView.setUrl(QtCore.QUrl(url))

		#tagapp = extract_tag.extract_tag()
		imgdir = IMAGEDIR#'/home/geunho/PycharmProjects/qweb/images/'
		self.tags, self.imgs = TAGS, IMGS
		self.textapp = recommender.extract_similarity()

		# history buttons:
		self.ui.back.setEnabled(False)
		self.ui.next.setEnabled(False)
		
		QtCore.QObject.connect(self.ui.back,QtCore.SIGNAL("clicked()"), self.back)
		QtCore.QObject.connect(self.ui.next,QtCore.SIGNAL("clicked()"), self.next)
		QtCore.QObject.connect(self.ui.url,QtCore.SIGNAL("returnPressed()"), self.url_changed)
		QtCore.QObject.connect(self.ui.webView,QtCore.SIGNAL("linkClicked (const QUrl&)"), self.link_clicked)
		QtCore.QObject.connect(self.ui.webView,QtCore.SIGNAL("urlChanged (const QUrl&)"), self.link_clicked)
		QtCore.QObject.connect(self.ui.webView,QtCore.SIGNAL("loadProgress (int)"), self.load_progress)
		QtCore.QObject.connect(self.ui.webView,QtCore.SIGNAL("titleChanged (const QString&)"), self.title_changed)
#		QtCore.QObject.connect(self.ui.reload, QtCore.SIGNAL("clicked()"), self.reload_page)
		QtCore.QObject.connect(self.ui.reload, QtCore.SIGNAL("clicked()"),self.on_pushButton_clicked)
		QtCore.QObject.connect(self.ui.stop,QtCore.SIGNAL("clicked()"), self.stop_page)

#		self.pushButton = QtGui.QPushButton("click me")
#		self.pushButton.clicked.connect(self.on_pushButton_clicked)

		self.dialog = PictureFlow1()
		#images = listdir('/home/geunho/caffe_SSDH/examples/SSDH/')
		#for i in images:
		#	if i.endswith('jpg'):
		#		self.dialog.addSlide(QtGui.QPixmap('/home/geunho/caffe_SSDH/examples/SSDH/%s' % i))

		QtCore.QMetaObject.connectSlotsByName(self)

	def on_pushButton_clicked(self):
		import pandas as pd
		#text = pd.read_clipboard(header=None).values
		text = pd.read_clipboard(header=None)
		str1=''
		for i in range(0, text.shape[1]):
			str1=str1+text[i][0]+' '

		print(str1)

		self.dialog = PictureFlow1()
		tags = self.tags
		ranking = self.textapp.text_similarity(tags,str1)

		self.dialog.rank = ranking
		self.dialog.imgs_rank = self.imgs


		#images = listdir('/home/geunho/caffe_SSDH/examples/SSDH/')

		for i in range(0, 20): #keypoint
			idx = ranking[i]
			self.dialog.addSlide(QtGui.QPixmap(self.imgs[idx]))

		df = pd.DataFrame(['파일경로'])
		df.to_clipboard(index=False, header=False)

		self.dialog.show()

	def url_changed(self):
		"""
		Url have been changed by user
		"""
		page = self.ui.webView.page()
		history = page.history()
		if history.canGoBack():
			self.ui.back.setEnabled(True)
		else:
			self.ui.back.setEnabled(False)
		if history.canGoForward():
			self.ui.next.setEnabled(True)
		else:
			self.ui.next.setEnabled(False)
		
		url = self.ui.url.text()
		self.ui.webView.setUrl(QtCore.QUrl(url))
		
	def stop_page(self):
		"""
		Stop loading the page
		"""
		#self.ui.webView.stop()

		df = pd.DataFrame(['Text to copy'])
		df.to_clipboard(index=False, header=False)
		print(df)
	
	def title_changed(self, title):
		"""
		Web page title changed - change the tab name
		"""
		self.setWindowTitle(title)
	
	def reload_page(self):
		"""
		Reload the web page
		"""
		#self.ui.webView.setUrl(QtCore.QUrl(self.ui.url.text()))

		import pandas as pd
		text = pd.read_clipboard(header=None).values
		print(text)
		textapp = recommender.extract_similarity()
		tags = self.tags
		ranking = textapp.text_similarity(tags, text)
		self.dialog.rank = ranking
		self.dialog.imgs_rank = self.imgs

		df = pd.DataFrame(['파일경로'])
		df.to_clipboard(index=False, header=False)



	def link_clicked(self, url):
		"""
		Update the URL if a link on a web page is clicked
		"""
		page = self.ui.webView.page()
		history = page.history()
		if history.canGoBack():
			self.ui.back.setEnabled(True)
		else:
			self.ui.back.setEnabled(False)
		if history.canGoForward():
			self.ui.next.setEnabled(True)
		else:
			self.ui.next.setEnabled(False)
		
		self.ui.url.setText(url.toString())
	
	def load_progress(self, load):
		"""
		Page load progress
		"""
		if load == 100:
			self.ui.stop.setEnabled(False)
		else:
			self.ui.stop.setEnabled(True)
		
	def back(self):
		"""
		Back button clicked, go one page back
		"""
		'''back-geunho'''

		page = self.ui.webView.page()
		history = page.history()
		history.back()
		if history.canGoBack():
			self.ui.back.setEnabled(True)
		else:
			self.ui.back.setEnabled(False)
	
	def next(self):
		"""
		Next button clicked, go to next page
		"""
		page = self.ui.webView.page()
		history = page.history()
		history.forward()
		if history.canGoForward():
			self.ui.next.setEnabled(True)
		else:
			self.ui.next.setEnabled(False)

	def contextMenuEvent(self, event):
		self.menu = QtGui.QMenu(self)
		renameAction = QtGui.QAction('Rename', self)
		renameAction.triggered.connect(lambda: self.renameSlot(event))
		self.menu.addAction(renameAction)
		# add other required actions
		self.menu.popup(QtGui.QCursor.pos())


	def mousePressEvent(self, event):
		"""
		mouse clicks events
		"""
		button = event.button()
		item = self.itemAt(event.x(), event.y())
		if item:
			# select the item we clicked
			self.setCurrentItem(item)
			if button == 1:
				print 'LEFT CLICK - DRAG'
		if button == 2:
			print 'RIGHT CLICK'

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	tagapp = extract_tag.extract_tag()

	IMAGEDIR = './images/'#'/home/geunho/PycharmProjects/qweb/images/'
	TAGS, IMGS = tagapp.image_tag(IMAGEDIR)
	#self.textapp = recommender.extract_similarity()

	myapp = httpWidget()
	myapp.show()
	sys.exit(app.exec_())
