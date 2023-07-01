from django import forms
from app.models import *


class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'


class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        #fields='__all__'
        #fields=('topic_name','name')
        exclude=['email']
        #help_texts={'name':'  Name should start with capital letter'}
        labels={'name':'Enter Name','url':'Enter URL '}
        widgets={'name':forms.PasswordInput,'url':forms.Textarea}

class AccessForm(forms.ModelForm):
    class Meta:
        model=Access
        fields='__all__'