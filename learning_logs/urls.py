
from django.urls import path, re_path
from learning_logs import views


# 不写runserver时会报错
app_name = 'learning_logs'

urlpatterns = [
    # html使用模板得加上name不写runserver时会报错,name可以看做是视图函数的别名,而reverse()参数逆向解析就是用的这个别名
    # 第一个参数是正则表达式，第二个参数指定调用视图，第三个参数指定名称
    path('', views.index, name='index'),
    # 显示所有的主题
    path('topics/', views.topics, name='topics'),
    # 特定主题的详细页面,使用正则表达式要用re_path否则会报警告
    re_path('topics/(?P<topic_id>\d+)/', views.topic, name='topic'),
    # 用于添加新主题的网页
    path('new_topic/', views.new_topic, name='new_topic'),
    # 用于添加新条目的页面
    re_path('new_entry/(?P<topic_id>\d+)/', views.new_entry, name='new_entry'),
    # 用于编辑条目的页面
    re_path('edit_entry/(?P<entry_id>\d+)/', views.edit_entry, name='edit_entry'),
]