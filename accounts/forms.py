from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs['class'] = 'form-control'
      field.widget.attrs['placeholder'] = field.label

class SignUpForm(forms.Form):
  username = forms.CharField(widget=forms.TextInput)
  password = forms.CharField(widget=forms.PasswordInput)
  confirmation_password = forms.CharField(widget=forms.PasswordInput)

  def clean_username(self):
    username = self.cleaned_data.get('username')
    print('#########')
    print(username)
    print(self.cleaned_data)
    if User.objects.filter(username=username).exists():
      raise forms.ValidationError('The username has been already taken.')
    return username

  def clean_enter_password(self):
    password = self.cleaned_data.get('password')
    print('#########')
    print(password)
    print(self.cleaned_data)
    if len(password) < 5:
      raise forms.ValidationError('Password must contain 5 or more characters.')
    return password

  def clean(self):
    super(SignUpForm, self).clean()
    password = self.cleaned_data.get('enter_password')
    retyped = self.cleaned_data.get('retype_password')
    if password and retyped and (password != retyped):
      self.add_error('retype_password', 'This does not match with the above.')

  def save(self):
    username = self.cleaned_data.get('username')
    password = self.cleaned_data.get('enter_password')
    new_user = User.objects.create_user(username=username)
    new_user.set_password(password)
    new_user.save()
