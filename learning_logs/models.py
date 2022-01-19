from django.db import models
from django.contrib.auth.models import User


# Create your models here. 模型告诉Django如何处理应用程序中存储的数据
# 用户将要存储的主题的模型

class Topic(models.Model):
    """用户学习的主题"""
    # 可存储少量文本由字符或文本组成，需预留存储空间
    text = models.CharField(max_length=200)
    # 记录日期和时间 参数为自动设置为当前日期和时间
    data_added = models.DateTimeField(auto_now_add=True)
    # 添加一个关联到用户的外键
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    # 外键 将每个条目关联到特定主题，获取与特定主题相关联的条目
    # 注意：django 升级到2.0之后,表与表之间关联的时候,必须要写on_delete参数,否则会报异常
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    # 按创建顺序呈现条目，并在每个条目旁边放置时间戳
    data_added = models.DateTimeField(auto_now_add=True)

    # 存储用于管理模型的额外信息
    class Meta:
        # 设置一个特殊属性，让Django在需要时使用Entries 来表示多个条目
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        # 只显示text的前50个字符
        return self.text[:50] + "..."