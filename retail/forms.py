from django import forms

class NicknameForm(forms.Form):
    nickname = forms.CharField(label='NICKNAME', label_suffix='', max_length=20)
