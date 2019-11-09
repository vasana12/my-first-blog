from threading import Thread
from polls.engine.analyser.crawlLibNaverBlog import *
from polls.engine.analyser.textAnalyzer import *
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

def alm3_analyzer(pollsBreakdown, DIR_PATH):

    keyword1 = pollsBreakdown.keywordA[0]
    keyword2 = pollsBreakdown.keywordB[0]

    channelA = pollsBreakdown.channelA[0]
    channelB = pollsBreakdown.channelB[0]

    startDate1 = pollsBreakdown.periodA[0]
    endDate1 = pollsBreakdown.periodA[1]
    startDate2 = pollsBreakdown.periodB[0]
    endDate2 = pollsBreakdown.periodB[1]


    nUrlA = int(pollsBreakdown.nUrlA)
    nUrlB = int(pollsBreakdown.nUrlB)
    #### 각 키워드의 빈도표 보여주기

    analyzer1 = TextAnalyzer(keyword1, channelA, startDate1, \
                            endDate1, "Okt", nUrlA)

    dict1 = analyzer1.extractFrequentWords(500, 5)
    print("<" + keyword1 + ">")
    print(dict1)

    wc1 = WordCloudRenderer(dict1, 'Dark2')

    analyzer2 = TextAnalyzer(keyword2, channelB, startDate2, \
                            endDate2, "Okt", nUrlB)
    dict2 = analyzer2.extractFrequentWords(500, 5)
    print("<" + keyword2 + ">")
    print(dict2)

    wc2 = WordCloudRenderer(dict2, 'tab10', DIR_PATH)

    wc1.draw(1, keyword1)
    wc2.draw(2, keyword2)

    ## 차이 분석 ##


    sc = setCalc(dict1, dict2)
    interdict = sc.getInter()
    differa = sc.getDiff1()
    differb = sc.getDiff2()

    # print("<%s - %s>" % (keyword1, keyword2))
    # print(differa)
    #
    # print("<%s - %s>" % (keyword2, keyword1))
    # print(differb)
    #
    # print("<intersection between %s and %s>" % (keyword2, keyword1))
    # print(interdict)

    wc3 = WordCloudRenderer(differa, 'Dark2')
    wc4 = WordCloudRenderer(differb, 'tab10')

    wc3.draw(3, keyword1+'-'+keyword2)
    wc4.draw(4, keyword2+'-'+keyword1)

    ###### 벤다이어그램 ######


    wc5 = WordCloudRenderer(interdict, 'brg')
    wc5.setMask("./mask_inter.png")

    wc6 = WordCloudRenderer(differa, 'Dark2')
    wc6.setMask("./mask_diff1.png")

    wc7 = WordCloudRenderer(differb, 'tab10')
    wc7.setMask("./mask_diff2.png")

    # 교집합그림#
    plt.figure(5, figsize=(16, 12))
    plt.imshow(wc5.getWordCloud(), interpolation='bilinear')
    plt.imshow(wc6.getWordCloud(), interpolation='bilinear')
    plt.imshow(wc7.getWordCloud(), interpolation='bilinear')

    plt.axis('off')
    print(DIR_PATH+'/'+keyword1+'_inter_'+keyword2)
    plt.savefig(DIR_PATH+'/'+keyword1+'_inter_'+keyword2)
    plt.show()
