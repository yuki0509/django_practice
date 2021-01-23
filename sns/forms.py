from django import forms
from . models import Message, Group, Friend, Good
from django.contrib.auth.models import User

class MessageForm(forms.ModelForm):
  class Meta:
    model = Message
    fields = ['owner', 'group', 'content']

class GroupForm(forms.ModelForm):
  class Meta:
    model = Group
    fields = ['owner', 'title']

class FriendForm(forms.ModelForm):
  class Meta:
    model = Friend
    fields = ['owner', 'user', 'group']

class GoodForm(forms.ModelForm):
  class Meta:
    model = Good
    fields = ['owner', 'message']

#Groupのチェックボックスフォーム
class GroupCheckForm(forms.Form):
  def __init__(self, user, *args, **kwargs)
    super(GroupCheckForm, self).__init__(*args, **kwargs)
    public = User.objects.filter(username='public').first()
    self.fields['groups'] = forms.MultipleChoiceField(
      choices=[(item.title, item.title) for item in Group.objects.filter(owner__in=[user, public])], widget=forms.CheckboxSelectMultiple(),
    )

#Groupの選択メニューフォーム
class GroupSelectForm(forms.Form):
  def __init__(self, user, *args, **kwargs):
    super(GroupSelectForm, self).__init__(*args, **kwargs)
    self.fields['groups'] = forms.ChoiceField(
      choices=[('-','-')] + [(item.title, item.title) for item in Group.objects.filter(owner=user)], widget=forms.Select(attrs={'class':'form-control'}),
    )

class FriendForm(forms.Form):
  def __init__(self, user, friends=[], vals=[], *args, **kwargs):
    super(FriendForm, self).__init__(*args, **kwargs)
    self.fields['friends'] = forms.MultipleChoiceField(
      choices=[(item.user, item.user) for item in friends],widget=forms.CheckboxSelectMultiple(), initial=vals
    )

class CreateGroupForm(forms.Form):
  group_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))

class PostForm(forms.Form):
  content = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'class':'form-control'}))

  def __init__(self, user, *args, **kwargs):
    super(PostForm, self).__init__(*args, **kwargs)
    public = User.objects.filter(username='public').first()
    self.fields['groups'] = forms.ChoiceField(
      choices=[('-','-')] + [(item.title, item.title) for item in Group.objects.filter(owner__in=[user, public])], widget=forms.Select(attrs={'class':'form-control'}),
    )
