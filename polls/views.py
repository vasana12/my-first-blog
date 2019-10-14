from django.shortcuts import render
from django.http import HttpResponse
from .models import Breakdown
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from polls.engine.analyser import crawlLibNaverBlog, textAnalyzer
from polls.engine.crawler import setting, dao
import os

def table(request):
    return render(request, 'polls/table.html')

def charts(request):
    return render(request, 'polls/charts.html')

def test(request):
    return render(request, 'polls/test.html')

def index(request):
    return render(request, 'polls/index.html')

def home(request):
    return render(request, 'polls/home.html')

# Create your views here.
def all(request):
    return render(request, 'polls/all.html')

def keyword(request):
    return render(request, 'polls/keyword.html')

def channel(request):
    return render(request, 'polls/channel.html')

def period(request):
    return render(request, 'polls/period.html')

def submit(request):
    breakdown = dao.dao(request)

    setting.crawler(breakdown)
    #
    # # 키워드 비교 크롤러
    #     # # 1. setting 인스턴스 생성
    #DIR_PATH = os.path.dirname(os.path.realpath(__file__)) + "\\static\\polls\\source\\"
    #print('DIR_PATH=', DIR_PATH)


    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #setting = Setting(DIR_PATH, select.id)
    #wc = AlmadenAnalyser(select.id, channelA_checked, keywordA, periodA, channelB_checked, keywordB, periodB, setting)
    #
    #wc.run_crawlers(5)  # 크롤링 개수

    #wc.load_data()
    #wc.run_gapAnalysis()

    ##### URL List 생성
    # delete from urllist
    # delete from htdocs
    return HttpResponseRedirect(reverse('polls:results', args=(breakdown.id,)))


class ResultsView(generic.DetailView):
    model = Breakdown
    template_name = 'polls/results.html'
