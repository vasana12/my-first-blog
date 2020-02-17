from django.shortcuts import render
from django.http import HttpResponse
from .models import PollsBreakdown, AuthUser
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from polls.engine.analyser import crawlLibNaverBlog, textAnalyzer
from polls.engine.crawler import setting, dao
import os
from datetime import datetime
from django.http import Http404
from django.shortcuts import render

from django.shortcuts import render_to_response
from django.contrib.auth import login, authenticate
from .forms import LoginForm
from django.contrib import messages

def table(request):
    return render(request, 'polls/table.html')

def charts(request):
    return render(request, 'polls/charts.html')

def test(request):
    return render(request, 'polls/test.html')

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

def word(request):
    usr_id = request.session.get('id')

    try :
        wordcloud = PollsBreakdown.objects.filter(usr_key=usr_id)
    except PollsBreakdown.DoesNotExist:
        raise Http404("WordCloud does not exist")
    return render(request, 'polls/results.html',
                  {'wordcloud': wordcloud})


def login(request):
    if request.method == 'POST':
    # Data bounded form인스턴스 생성
        login_form = LoginForm(request.POST)
    # form으로부터 username, password값을 가져옴

    usr_id = request.POST['usr_id']
    password = request.POST['password']
    try:
        user = AuthUser.objects.get(username=usr_id)
    except (KeyError, AuthUser.DoesNotExist):
        login_form.add_error(None, '아이디 또는 비밀번호가 올바르지 않습니다')

    try:
        if user is not None:
            if password == user.password:
                request.session['id']=user.id
                print(request.session['id'])
                return HttpResponseRedirect(reverse('polls:detail', args=(user.id,)))
            else:
                return render(request, 'polls/home.html',{'error_message': "password error"})
    except (KeyError, AuthUser.DoesNotExist):

        return render(request, 'polls/home.html', {'error_message': "id or pass error"})

    else:
        return render(request, 'polls/home.html', {'error_message': "id or pass error"})
    return render(request, 'polls/home.html')


class DetailAll(generic.DetailView):

    model = AuthUser
    template_name = 'polls/all.html'

class DetailView(generic.DetailView):
    model = AuthUser
    template_name = 'polls/base.html'

def submit(request):
    print('submit이다')
    username = request.POST['username']
    print(username)
    usr_key = request.POST['usr_key']
    print(usr_key)
    pollsBreakdown = dao.breakdown_dao(request)
    print('submit', pollsBreakdown.id)
    print(pollsBreakdown.channelA[0])
    setting.crawler(pollsBreakdown)


    ##textAnalyzer

    #
    # # 키워드 비교 크롤러
    #     # # 1. setting 인스턴스 생성
    DIR_PATH = os.path.dirname(os.path.realpath(__file__)) + "\\static\\polls\\source\\image"
    print('DIR_PATH=', DIR_PATH)

    setting.analyzer(pollsBreakdown, DIR_PATH)
    authuser = AuthUser.objects.get(id=usr_key)
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
    return HttpResponseRedirect(reverse('polls:word'))


class ResultsView(generic.DetailView):
    model = PollsBreakdown
    template_name = 'polls/test.html'
