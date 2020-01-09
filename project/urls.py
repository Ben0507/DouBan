from django.conf.urls import url
from . import views

urlpatterns = [
    url('home/', views.home, name="home"),
    url('details/',views.details,name="details"),
    url('list/',views.list,name="list"),
    url('^search/$',views.search,name="search"),
    url('^showsearch/$',views.showsearch,name="showsearch"),
    url('register/', views.register, name="register"),
    url('logins/', views.logins, name="logins"),
    url('forget/', views.forget, name="forget"),
]
