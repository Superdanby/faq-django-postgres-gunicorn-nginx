from django.db import models
from django.conf import settings

import os

# Create your models here.
class FAQ(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    question_text = models.CharField(max_length=10000)
    answer_text = models.TextField()

    def __str__(self):
        return self.question_text + self.answer_text


class Images(models.Model):
    faq = models.ForeignKey(FAQ, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images')

    def __str__(self):
        return self.img.url


class Files(models.Model):
    faq = models.ForeignKey(FAQ, on_delete=models.CASCADE)
    f = models.FileField(upload_to='files')

    def __str__(self):
        return self.f.url

    def filename(self):
        return os.path.basename(self.f.name)
