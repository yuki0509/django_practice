from django import forms

class HelloForm(forms.Form):
  data = [
    ('one', 'item 1'),
    ('two', 'item 2')
  ]
  choice = forms.ChoiceField(label='Choice', choices=data, widget=forms.RadioSelect())
