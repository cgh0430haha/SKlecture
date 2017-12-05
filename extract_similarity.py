# -*- coding: utf-8 -*-
# coding: cp949
import fastText
import numpy as np
from sklearn import metrics
from watson_developer_cloud import NaturalLanguageUnderstandingV1 as NaturalLanguageUnderstanding
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions

import cv2
import extract_tag


class extract_similarity():
    def __init__(self, parent=None):
        self.f = fastText.load_model('./wiki.ko.bin') #keypoint
                #'/home/geunho/PycharmProjects/qweb/wiki.ko.bin'
        self.NLU = NaturalLanguageUnderstanding(
                url="https://gateway.aibril-watson.kr/natural-language-understanding/api",
                username="e382e220-1d91-4fcc-81e1-75aee1fa08a3",
                password="5eYRH35owwn0",
                version="2017-02-27") 
        
    def text_similarity(self,imgtag,text0):        
        response = self.NLU.analyze(
                text=text0,
                features=Features(keywords=KeywordsOptions(limit=10)))         
        textout=[]
        for i in xrange(len(response['keywords'])):
            textout.append(response['keywords'][i]['text'])
        
        maxlen=0
        for i1 in xrange(len(imgtag)):
            if maxlen<len(imgtag[i1]):
                maxlen=len(imgtag[i1])                
        t_s = np.zeros([len(imgtag),maxlen,len(textout)])        
        
        for i1 in xrange(len(imgtag)):
            for i2 in xrange(len(imgtag[i1])):
                for j in xrange(len(textout)):                
                    f1vector = self.f.get_word_vector(textout[j])
                    f2vector = self.f.get_word_vector(imgtag[i1][i2])
                    co_si=metrics.pairwise.cosine_similarity([f1vector],[f2vector])
                    t_s[i1,i2,j]=co_si[0][0]        
        similar = t_s.max(1).max(1)
        ranking = np.flip(similar.argsort(),0)   
        return ranking
                    
                    
if __name__ == "__main__":
    tagapp = extract_tag.extract_tag()
    textapp = extract_similarity()
    
    imgdir = '' #''/home/geunho/PycharmProjects/qweb/images/'
    tags,imgs = tagapp.image_tag(imgdir)    
    ttext = ' 설레는 마음을 안고 비행기에 올라 비행기 밖의 풍경도 찍고(구름 밖에 없지만요), 기내에서 나오는 기내식도 아주 맛있게 먹었습니다. 저는 불고기 쌈밥을 선택했네요. 생각보다 맛있었어요. 그리고 약 12시간의 비행기 여행을 마치고, 드디어 런던 공항에 도착을 했습니다! 도착한 시간이 이른 아침이었는데, 비행기에서 푹 잔 덕분인지 여행에 대한 기대감 때문인지 공항에 내리는 순간부터 정신이 멀쩡해졌어요. 그리고 짐을 재빨리 찾고 나왔습니다. '
    ranking = textapp.text_similarity(tags,ttext)
     
    for i in xrange(10):
        cv2.imshow(str(i),imgs[ranking[i]])
        cv2.waitKey(10)
        
        
    
    
