from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView,DetailView
from django.contrib import messages
from . import models
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required
from .models import Question, Answer

class QuestionListView(ListView):

    context_object_name = 'questions'
    model = models.Question
    template_name = 'questions_list.html'


def question_detail(request, slug=None):
    question = get_object_or_404(Question, slug=slug)
    answers_list = Answer.objects.filter(question=question)
    context = { "question": question,
                "answers_list": answers_list,
                 }

    if request.user.is_authenticated:
        form = AnswerForm(request.POST or None)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            form = AnswerForm()    
            return redirect(question.get_absolute_url())
        context = { "question": question,
                    "form": form,
                    "answers_list": answers_list,
                  }
    return render(request, "questions/question_detail.html", context)

@login_required()
def question_ask(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        question = form.save(commit=False)
        question.user = request.user
        question.save()
        return redirect("questions:question_list")

    context = { "form": form,
                "title": "Ask Question"
              }
    return render(request, "questions/ask.html", context)


