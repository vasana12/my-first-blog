from django.urls import path
from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.home, name='home'),

    path('index', views.index, name='index'),

    path('test', views.test, name='test'),

    # ex:/all
    path('all', views.all, name='all'),

    # ex:/keyword
    path('keyword', views.keyword, name='keyword'),

    # ex:/channel
    path('channel', views.channel, name='channel'),

    # ex:/period
    path('period', views.period, name='period'),

    # ex:/polls/submit
    path('submit', views.submit, name='submit'),

    path('table', views.table, name='table'),

    path('charts', views.charts, name='charts'),
    # ex:/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results')
]