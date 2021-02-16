from django import forms


class URLForm(forms.Form):
    initial_url = forms.CharField(label="Original URL", max_length=1000)
    shortened = forms.CharField(label="Short Name", max_length=10)
