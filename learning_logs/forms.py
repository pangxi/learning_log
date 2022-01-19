from django import forms

from learning_logs.models import Topic,Entry


class TopicForm(forms.ModelForm):
    # 告诉Django根据哪个模型创建表单，以及在表单中包含哪些字段
    class Meta:
        # 告诉Django根据哪个模型创建表单
        model = Topic
        # 该表单只包含字段text
        fields = ['text']
        # 让Django不要为字段text生成标签
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        # 告诉Django根据哪个模型创建表单
        model = Entry
        # 该表单只包含字段text
        fields = ['text']
        # 让Django不要为字段text生成标签
        labels = {'text': ''}
        # 设置属性widgets覆盖Django选择的默认小部件。forms.Textarea定制了字段'text'输入小部件，本区域宽度设置为80列
        widgets = {'text':forms.Textarea(attrs={'cols':80})}



