from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm  # 默认表单
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse




# Create your views here.

def logout_view(request):
    """注销用户"""
    # 调用了函数logout()
    logout(request)
    # 重定向到主页
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 显示空的注册表单，不给它提供任何初始数据
        form = UserCreationForm()
    else:   # 点击提交，录入信息，切换登录状态，转到主页
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,password=request.POST['password1'])
            login(request,authenticated_user)
            # 重定向到主页
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form':form}
    return render(request,'register.html',context)




