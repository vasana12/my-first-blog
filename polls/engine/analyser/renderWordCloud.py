from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os


class WordCloudRenderer:
    def __init__(self, d, pal, DIR_PATH):
        self.dir = DIR_PATH
        self.dict = dict(d)
        self.maskPic = np.array(Image.open(self.dir+"/"+"mask.png"))
        self.palette=pal

    def setMask(self, filename):
        self.maskPic = np.array(Image.open(filename))

    def getWordCloud(self):
                              ## NanumBarunGothic.ttf', 
        wordcloud = WordCloud(font_path='c:/Windows/Fonts/NanumBarunGothic.ttf',\
                              background_color="rgba(255, 255, 255, 0)", mode="RGBA",\
                              max_font_size=120, \
                              min_font_size=18, \
                              mask=self.maskPic, \
                              width=800, height=600, \
                              colormap=self.palette)\
                    .generate_from_frequencies(self.dict)
        return wordcloud
    
        
    def draw(self, index , keyword):
        wordcloud = WordCloud(font_path='c:/Windows/Fonts/NanumBarunGothic.ttf',\
                              background_color='rgba(255, 255, 255, 0)', mode="RGBA", \
                              max_font_size=120, \
                              min_font_size=18, \
                              mask=self.maskPic, \
                              width=800, height=600, \
                              colormap=self.palette)\
                    .generate_from_frequencies(self.dict)

        plt.figure(index, figsize=(12, 12))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.savefig(self.dir+'\\image\\'+keyword)
