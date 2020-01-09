from django.db import models


# Create your models here.
# 电影详情
class movie_detail(models.Model):
    movie_details_id = models.AutoField(primary_key=True)
    movie_id = models.AutoField
    moviename = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    center = models.CharField(max_length=12000)
    introduction = models.CharField(max_length=3000)

    class Meta:
        db_table = 'movie_details'


class movielist(models.Model):
    movie_id = models.AutoField(primary_key=True)
    mname = models.CharField(max_length=50)
    mphoto = models.CharField(max_length=500)
    score = models.FloatField()
    url = models.CharField(max_length=400)

    class Meta:
        db_table = 'movielist'


# 电影短评
class movie_short(models.Model):
    movie_short_id = models.AutoField(primary_key=True)
    movie_details_id = models.IntegerField(max_length=3)
    username = models.CharField(max_length=100)
    head = models.CharField(max_length=200)
    comment_time = models.CharField(max_length=100)
    short = models.CharField(max_length=8000)

    class Meta:
        db_table = 'movie_short'

# 电影详情
class movie_actor(models.Model):
    movie_actor_id = models.AutoField(primary_key=True)
    movie_details_id = models.IntegerField(max_length=3)
    name  = models.CharField(max_length=50)
    head = models.CharField(max_length=400)
    role = models.CharField(max_length=100)


    class Meta:
        db_table = 'movie_actor'
#用户信息表
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=64)
    key=models.CharField(max_length=20)
    class Meta:
        db_table = 'movie_user'