from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
User = settings.AUTH_USER_MODEL

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qus = models.CharField(max_length=256, verbose_name="question")
    details = models.TextField(blank=True)
    slug = models.SlugField(unique=True, max_length=256)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.qus

    def get_absolute_url(self):
        return reverse("questions:question_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['-created']

    def _get_unique_slug(self):
        slug = slugify(self.qus)
        unique_slug = slug
        num = 1
        while Question.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(Question, self).save()


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    ans = models.TextField(verbose_name="answer")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ans

    class Meta:
        ordering = ['-created']
