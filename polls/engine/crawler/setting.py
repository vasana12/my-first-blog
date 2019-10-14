from polls.engine.analyser import crawlLibNaverBlog, textAnalyzer
from threading import Thread
from ..analyser import channel_crawl

def crawler(breakdown):

        channel_crawl.select_channel(int(breakdown.nUrlA), breakdown.keywordA[0], breakdown.channelA[0], breakdown.periodA[0], breakdown.periodA[1])
        channel_crawl.select_channel(int(breakdown.nUrlB), breakdown.keywordB[0], breakdown.channelB[0], breakdown.periodB[0], breakdown.periodB[1])
