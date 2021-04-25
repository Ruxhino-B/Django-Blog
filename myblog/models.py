from django.db import models
from perdorues.models import Perdorues
from django.urls import reverse
from datetime import datetime, date
# Create your models here.

class Post(models.Model):
    titull = models.CharField(max_length=255)
    autor = models.ForeignKey(Perdorues, on_delete=models.CASCADE, related_name='autoret')
    trupi = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(Perdorues, related_name='post_like')

    def __str__(self):
        return self.titull + ' | ' + self.autor.username
    def get_absolute_url(self):

        return reverse('post_detail', args=(str(self.id)))
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


