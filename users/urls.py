
from django.urls import path, re_path
from django.contrib.auth.views import LoginView   # 导入默认视图LoginView
from users import views

"""为应用程序users定义URL模式"""

# 不写runserver时会报错
app_name = 'users'
# URL模式是一个对函数path的调用，第一个参数是正则表达式，第二个参数指定调用视图，第三个参数指定名称
# 当需要提供到这个主页的链接时，都将使用这个名称而不是编写URL
urlpatterns = [

    # 登录页面 鉴于没有编写视图函数而是使用默认的LoginView，后面的as_view告诉django去哪里寻找模板
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('register/',views.register,name='register')
]