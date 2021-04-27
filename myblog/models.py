from django.db import models
from perdorues.models import Perdorues
from django.urls import reverse
from datetime import datetime, date
# Create your models here.

class Kategori(models.Model):
    emer = models.CharField(max_length=250)
    def __str__(self):
        return self.emer
    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    choices = Kategori.objects.all().values_list('emer','emer')
    choice_list = []
    for element in choices:
        choice_list.append(element)
    titull = models.CharField(max_length=255)
    autor = models.ForeignKey(Perdorues, on_delete=models.CASCADE, related_name='autoret')
    trupi = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(Perdorues, related_name='post_like')
    katekoria = models.CharField(choices=choice_list, default='C', max_length=255)

    def __str__(self):
        return self.titull + ' | ' + self.autor.username
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
        #return reverse('home')
    def total_likes(self):
        return self.likes.count()

class Koment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='koment_post')
    komentues = models.ForeignKey(Perdorues, on_delete=models.CASCADE, related_name='koment_user')
    body = models.TextField()
    date_komenti = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post, self.komentues)


