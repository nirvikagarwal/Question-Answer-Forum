from django.urls import path,re_path
from .views import (QuestionListView, 
                    question_detail, add_comment_to_answer, comment_list_view,
                    question_ask)

app_name = 'questions'

urlpatterns = [
    
    path('', QuestionListView.as_view(), name='question_list'),
    path('ask/', question_ask , name='question_ask'),
    path('add_comment/<int:pk>',add_comment_to_answer, name='add_comment'),
    path('view_comments/<int:pk>',comment_list_view, name='comment_list'),
    re_path(r'^(?P<pk>\d+)', question_detail, name='question_detail'),
]
