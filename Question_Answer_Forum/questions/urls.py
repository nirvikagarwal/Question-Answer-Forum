from django.urls import path,re_path
from .views import (QuestionListView, 
                    question_detail,
                    question_ask,)

app_name = 'questions'

urlpatterns = [
    
    path('', QuestionListView.as_view(), name='question_list'),
    path('ask/', question_ask, name='question_ask'),
    re_path(r'^(?P<slug>[\w-]+)/$', question_detail, name='question_detail'),
]
