from polls.models import PollsBreakdown
from polls.engine.analyser import crawlLibNaverBlog, crawlLibYouTube, crawlLibNaverNews, crawlLibInstagram
from threading import Thread

def select_channel(nUrl, keyword, channel, stdate, endate, id) :

    print(nUrl, keyword, channel, stdate, endate, id)
    if channel == 'Naver Blog':
        urlLister1 = crawlLibNaverBlog.NaverBlogLister(nUrl, keyword, channel, stdate,endate, id)
        urlLister1.createNaverBlogUrlList()

        crawler1 = crawlLibNaverBlog.NaverBlogCrawler(keyword, channel, stdate, endate, id)
        th1 = Thread(target=crawler1.crawlUrlTexts)
        th1.start()
        th1.join()

    elif channel == 'YouTube':
        urlLister1 = crawlLibYouTube.YouTubeCrawler('TO', channel, id)
        urlLister1.openBrowser()
        urlLister1.getVideoItems(keyword, nUrl, stdate, endate, id)
        urlLister1.closeBrowser()

        ytVideoList = urlLister1.readUrlListFromDB(keyword, id)

        nThread = 4
        urlLists = []
        ytContentList = []
        ytCrawlers = []
        for i in range(0, nThread):
            urlLists.append([])
            ytContentList.append([])
            ytc = crawlLibYouTube.YouTubeCrawler('T%d   ' % (i), channel, id)
            ytCrawlers.append(ytc)
            ytc.openBrowser()
        idx=0
        for v in ytVideoList:
            urlListNo = idx % nThread
            urlLists[urlListNo].append(v)
            idx +=1
        th = []
        for i in range(0, nThread):
            th.append(Thread(target=ytCrawlers[i].storeContentsIntoList, args=(urlLists[i], ytContentList[i])))
        for i in range(0, nThread):
            th[i].start()

        for i in range(0, nThread):
            th[i].join()

        for i in range(0, nThread):
            print(
                "\n\n========================================================================================================\n\nAt List ",
                i)
            for ycItem in ytContentList[i]:
                print("\n\n<", ycItem.title[0:30], "> : nReply=", ycItem.nReply)
                print(ycItem.titleDesc[0:30])
                for c in ycItem.comments:
                    print(">>", c.publishTime, c.text[0:30])

        for i in range(0, nThread):
            ytCrawlers[i].writeDocsToDB(keyword, channel, ytContentList[i])

        for i in range(0, nThread):
            ytCrawlers[i].closeBrowser()

    elif channel == 'Naver_News':
        s_page = 1
        maxpage = round(nUrl/10)

        crawler1 = crawlLibNaverNews.NaverNewsLister(s_page, maxpage, keyword, channel, stdate, endate, id)
        # crawler2 = NaverNewsLister(round((s_page+maxpage)/2), maxpage/2+1, keyword, channel, startDate, endDate)

        crawler1.crawler()

    elif channel == 'Instagram':
        instagramLister =crawlLibInstagram.InstagramLister(nUrl, keyword, channel, id)
        instagramLister.getInstagramUrl()
        itcrawler = crawlLibInstagram.InstagramCrawler(keyword,channel, id)
        itcrawler.crawlUrlTexts()