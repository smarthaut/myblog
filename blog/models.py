from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
#分类
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    #标签
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Post(models.Model):
    #标题
    title = models.CharField(max_length=100)
    #正文
    body = models.TextField()
    #创建时间，最后一次修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    #文章摘要
    excerpt = models.CharField(max_length=200,blank=True)
    #分类与标签
    category = models.ForeignKey(Category)
    tages = models.ManyToManyField(Tag,blank=True)
    #作者
    author = models.ForeignKey(User)
    def __str__(self):
        return self.title

    def get_url(self):
        #print( reverse(viewname='blog:detail',kwargs={'pk':self.pk}))
        return reverse(viewname='blog:detail',kwargs={'pk':self.pk})