from threading import Thread
from polls.engine.analyser.crawlLibNaverBlog import *
#from textAnalyzer import *
from polls.engine.analyser.renderWordCloud import *
from polls.engine.analyser.setCalculus import *
import matplotlib.pyplot as plt

########################################################################################################################

                                ##      ##        ##        ######    ##      ##
                                ####  ####      ##  ##        ##      ##      ##
                                ##  ##  ##    ##      ##      ##      ####    ##
                                ##  ##  ##    ##      ##      ##      ##  ##  ##
                                ##      ##    ##########      ##      ##    ####
                                ##      ##    ##      ##      ##      ##      ##
                                ##      ##    ##      ##    ######    ##      ##

########################################################################################################################



keyword1 = '홍삼스틱'


channel = 'Naver Blog'

startDate1 = '2017-01-01'
endDate1 = '2019-08-30'
nUrl = 1000


##### URL List 생성
# delete from urllist
# delete from htdocs

urlLister1 = NaverBlogLister(nUrl, keyword1, channel, startDate1, endDate1)


urlLister1.createNaverBlogUrlList()


