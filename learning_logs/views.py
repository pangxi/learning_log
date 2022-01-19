from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from learning_logs.forms import TopicForm,EntryForm
from learning_logs.models import Topic,Entry




# Create your views here.

def index(request):
    """学习笔记的主页"""
    return render(request,'index.html')
    # return HttpResponse('<p>Learning Log</p><p>Learning Log helps you keep track of your learning, for any topic youre learning about.</p>')

@login_required  # 检查用户是否已登录，如果用户未登录，就重定向到登录页面
def topics(request):
    """显示所有主题"""
    # topics = Topic.objects.order_by('data_added')

    # 查询数据库，请求提供Topic对象，只让所有者访问，按属性data_added进行排序
    topics = Topic.objects.filter(owner=request.user).order_by('data_added')
    # 键是将在模板中用来访问数据的名称，而值是要发送给模板的数据
    context = {'topics':topics}
    return render(request,'topics.html',context)

@login_required
def topic(request,topic_id):
    """显示单个主题及其所有的条目"""
    # 获取指定的主题
    topic = Topic.objects.get(id=topic_id)

    # 确认请求的主题属于当前用户，如主题不属于当前用户返回Http404页面
    if topic.owner != request.user:
        raise Http404

    # 获取与该主题相关联的条目
    entries = topic.entry_set.order_by('-data_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'topic.html',context)

@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据,对数据进行处理
        form = TopicForm(request.POST)
        # 检查填写了所有必不可少的字段（默认所有），且输入的数据与要求的类型一致
        if form.is_valid():
            # 表单中的数据写入数据库
            new_topic = form.save(commit=False)
            new_entry.owner = request.user
            new_topic.save()
            # 重定向到网页topics
            return HttpResponseRedirect(reverse('topics'))
    context = {'form': form}
    return render(request, 'new_topic.html', context)

@login_required
def new_entry(requset,topic_id):
    """在特定的主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)
    if requset.method != 'POST':
        # 未提交数据,创建一个空表单
        form = EntryForm()
    else:
        # POST提交的数据,对数据进行处理
        form = EntryForm(data=requset.POST)
        if form.is_valid():
            # 保存到new_entry中，但不保存到数据库中
            new_entry = form.save(commit=False)
            # 获取主题
            new_entry.topic = topic
            # 保存到数据库，与主题关联
            new_entry.save()
            # 列表args包含在URL中的所有实参，在这里只有一个
            return HttpResponseRedirect(reverse('topic',args=[topic_id]))
    context = {'topic':topic,'form':form}
    return render(requset,'new_entry.html',context)


@login_required
def edit_entry(request,entry_id):
    """编辑既有条目"""
    # 获取用户要修改的条目对象
    entry = Entry.objects.get(id=entry_id)
    # 关联该条目主题
    topic = entry.topic
    # 确认请求的主题属于当前用户，如主题不属于当前用户返回Http404页面
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # 初次请求，创建一个表单实例使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic',args=[topic.id]))
    context = {'entry':entry,'topic':topic,'form':form}
    return render(request,'edit_entry.html',context)

