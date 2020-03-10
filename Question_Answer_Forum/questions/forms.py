from django import forms
from questions.models import Question, Answer, Comment



class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question", "details"]

        widgets = {
            'question':forms.TextInput(attrs={'class':'form-control'}),
            'details':forms.Textarea(attrs={'class':'form-control'}),
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["answer"]
        widgets = {
            'answer':forms.Textarea(attrs={'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["comment"]

        widgets = {
            'comment':forms.Textarea(attrs={'class':'form-control'}),
        }


