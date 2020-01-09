from django.contrib.sessions.models import Session
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from project.models import *
import json


def home(request):
    movielists1 = movielist.objects.all()[:3]
    movielists2 = movielist.objects.all()[3:6]
    movielists3 = movielist.objects.all()[6:9]
    username = request.GET.get("username")
    request.session["username"] = username;
    return render(request, 'home/shouye.html',
                  {"username":username,"movielists1": movielists1, "movielists2": movielists2, "movielists3": movielists3})


def details(request):
    id = request.GET.get("id")
    # 显示电影详情
    detail = movie_detail.objects.filter(movie_details_id=id)
    # 显示短评
    movie_details_id = ""
    for i in detail:
        movie_details_id = i.movie_details_id
    short = movie_short.objects.filter(movie_details_id=movie_details_id)

    # 显示演员表
    actor = movie_actor.objects.filter(movie_details_id=movie_details_id)
    for i in short:
        i.short = i.short.decode("utf-8")

    return render(request, 'home/detail.html', {"detail": detail, "actor": actor, "short1": short})


# 返回电影列
def list(request):
    global movie
    movielists1 = movielist.objects.all()
    # 将数据按照规定每页显示 10 条, 进行分割
    paginator = Paginator(movielists1, 12)
    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page')
        try:
            movie = paginator.page(page)
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            movie = paginator.page(1)
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            movie = paginator.page(paginator.num_pages)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')

    return render(request, 'home/list.html', {'movie': movie,"username": request.session["username"]})


def search(request):
    if request.method == "GET":
        keyword = request.GET.get('select')
        movielist1= movielist.objects.filter(mname__startswith=keyword)
        name=[]
        for i in movielist1:
            name.append(i.mname)
        data = {
            "status": 200,
            "keyword": name
        }
        return HttpResponse(json.dumps(data))


def showsearch(request):
    if request.method == "GET":
        keyword = request.GET.get('select')
        print(keyword)
        movie = movielist.objects.filter(mname=keyword)
        return render(request, 'home/list.html', {'movie': movie})
# 登录
def logins(request):
    if request.method != 'POST':
        return render(request, 'home/logins.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    search_dict = dict()
    if len(username)and len(password)>0:
        if username:
            search_dict['username'] = username
        if password:
            search_dict['password'] = password
    # # 多条件查询 关键点在这个位置传如的字典前面一定要加上两个星号.
        user_all = User.objects.filter(**search_dict)
        if user_all:
            data = {
                'status': 200,
                'msg': username
            }
            return HttpResponse(json.dumps(data))
        else:
            data = {
                'status': 500,
                'msg': username
            }
            return HttpResponse(json.dumps(data))

    else:
        return render(request, 'home/logins.html')
#注册
def register(request):
    if request.method != 'POST':
        return render(request, 'home/register.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    key = request.POST.get('key')
    search_dict = dict()
    if username:
        search_dict['username'] = username
    # # 多条件查询 关键点在这个位置传如的字典前面一定要加上两个星号.
    user_all = User.objects.filter(**search_dict)
    if user_all:
        data = {
            'status': 500,
            'msg': 'fail'
            }
        return HttpResponse(json.dumps(data))
    elif str(user_all)=="<QuerySet []>":
        data = {
            'status': 200,
            'msg': 'success'
            }
        user = User()
        user.username = username
        user.key = key
        user.password = password  # my_md5(password)
        user.save()  # 保存对象
        return HttpResponse(json.dumps(data))
# 忘记密码
def forget(request):
    if request.method != 'POST':
        return render(request, 'home/forget.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    key = request.POST.get('key')
    search_dict = dict()
    if len(username)and len(password)>0:
        if username:
            search_dict['username'] = username
        if key:
            search_dict['key'] = key
    # # 多条件查询 关键点在这个位置传如的字典前面一定要加上两个星号.
        user_all = User.objects.filter(**search_dict)
        if user_all:
            User.objects.filter(username=username).update(password=password)
            data = {
                'status': 200,
                'msg': username
                }
            return HttpResponse(json.dumps(data))
        else:
            data = {
                 'status': 500,
                 'msg': 'fail'
                }
            return HttpResponse(json.dumps(data))
    else:
        return render(request, 'home/forget.html')
