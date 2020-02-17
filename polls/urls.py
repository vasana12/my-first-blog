from django.urls import path
from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.home, name='home'),

    path('test', views.test, name='test'),


    # ex:/keyword
    path('keyword', views.keyword, name='keyword'),

    # ex:/channel
    path('channel', views.channel, name='channel'),

    # ex:/period
    path('period', views.period, name='period'),

    # ex:/polls/submit
    path('submit', views.submit, name='submit'),

    path('login', views.login, name='login'),

    path('table', views.table, name='table'),

    path('charts', views.charts, name='charts'),

    # ex:/all
    path('word', views.word, name='word'),

    path('<int:pk>/all', views.DetailAll.as_view(), name='all'),

    path('<int:pk>/detail', views.DetailView.as_view(), name='detail'),
    # ex:/5/base/

    # ex:/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results')
]