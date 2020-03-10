from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.
User = settings.AUTH_USER_MODEL

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=256, verbose_name="question")
    details = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse("questions:question_detail", kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created']



class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField(verbose_name="answer")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer

    class Meta:
        ordering = ['-created']
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    comment = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

