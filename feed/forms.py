from django import forms # type: ignore

class PostForm(forms.Form):
    image = forms.FileField()
    title = forms.CharField()