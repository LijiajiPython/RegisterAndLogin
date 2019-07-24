from django.db import models
# from django.contrib import admin

# admin.site.site_header="没啥用的后台管理系统"
# admin.site.site_title="后台管理"
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32)
    date = models.DateField(auto_now=True)
    contend = models.TextField()
    description = models.TextField()
    author = models.ForeignKey(to="Author",on_delete=models.SET_DEFAULT,default=1)
    type = models.ManyToManyField(to="Type")
    class Meta:
        verbose_name_plural='文章'
    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.CharField(max_length=32)
    email = models.EmailField()
    class Meta:
        verbose_name_plural='作者'
    def __str__(self):
        return self.name

class Type(models.Model):
    name=models.CharField(max_length=32)
    description = models.TextField()
    class Meta:
        verbose_name_plural='文章种类'
    def __str__(self):
        return self.name

