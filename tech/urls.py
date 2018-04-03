"""tech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index),
    url(r'^questions/add$',views.AddQuestions.as_view()),
    url(r'^questions/list$',views.QuestionsList.as_view()),
    url(r'^questions/detail/(?P<question_id>[0-9]+)/$', views.QuestionsDetail.as_view()),
    url(r'^questions/edit$',views.QuestionsEdit.as_view()),
    url(r'^questions/report$',views.QuestionsReport.as_view()),
    url(r'^questions/list/by_module_name$',views.QuestionListByModule.as_view()),
    url(r'^questions/send_report$',views.SendReport.as_view())
]
