from polls.engine.analyser import crawlLibNaverBlog, textAnalyzer
from threading import Thread
from ..analyser import channel_crawl
from polls.engine.analyser.renderWordCloud import *
from polls.engine.analyser.setCalculus import *
from polls.engine.analyser.alm3_Analyzer import *
import matplotlib.pyplot as plt
import os

def crawler(pollsBreakdown):
    print('cralwer 진입')
    channel_crawl.select_channel(int(pollsBreakdown.nUrlA), pollsBreakdown.keywordA[0], pollsBreakdown.channelA[0],
                                 pollsBreakdown.periodA[0], pollsBreakdown.periodA[1], pollsBreakdown.id)

    channel_crawl.select_channel(int(pollsBreakdown.nUrlB), pollsBreakdown.keywordB[0], pollsBreakdown.channelB[0],
                                 pollsBreakdown.periodB[0], pollsBreakdown.periodB[1], pollsBreakdown.id)

def analyzer(pollsBreakdown, DIR_PATH):

    alm3_analyzer(pollsBreakdown, DIR_PATH)
