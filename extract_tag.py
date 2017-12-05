# -*- coding: utf-8 -*-
# coding: cp949
import csv  
import sys
import json
from os.path import join, dirname, realpath
from os import listdir
from os import environ
import watson_developer_cloud
from watson_developer_cloud import VisualRecognitionV3


class extract_tag():
    def __init__(self, parent=None):
        self.visual_recognition = VisualRecognitionV3('2016-05-20',api_key={'b9126c7c-ac1e-45ce-8b98-e44931a9f8e6:cLh7ZYXFrvBF'})
        self.visual_recognition.set_username_and_password('b9126c7c-ac1e-45ce-8b98-e44931a9f8e6', 'cLh7ZYXFrvBF')
        self.visual_recognition.set_url('https://gateway.aibril-watson.kr/visual-recognition/api')
        
    def image_tag(self,imagedir):
        self.images = listdir(imagedir)
        imgtag=[]
        imglist=[]
        for i in self.images:
            if i.endswith('jpg'):
                images_file=imagedir+i
                imglist.append(images_file)
                with open(images_file, 'rb') as images_file:
                    parameters = json.dumps({'threshold': 0.1, 'classifier_ids': ['CarsvsTrucks_1479118188', 'default']})
                    car_results = self.visual_recognition.classify(images_file=images_file,
                                                              parameters=parameters,accept_language='ko')
                tag=[]
                for i in xrange(len(car_results['images'][0]['classifiers'][0]['classes'])):
                    tag.append(car_results['images'][0]['classifiers'][0]['classes'][i]['class'])
                imgtag.append(tag)
        return imgtag,imglist
                    
                    
if __name__ == "__main__":
	tagapp = extract_tag()
	tags=tagapp.image_tag('')
	
    
    