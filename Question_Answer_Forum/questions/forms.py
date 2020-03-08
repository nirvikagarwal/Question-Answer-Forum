from django import forms
from .models import Question, Answer, Comment



class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["qus", "details"]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["ans"]

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["text"]

