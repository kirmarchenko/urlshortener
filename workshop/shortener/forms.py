from django import forms


class URLForm(forms.Form):
    """Здесь описываем какие данные будем получать через форму """
    initial_url = forms.CharField(label="Original URL", max_length=1000)
    shortened = forms.CharField(label="Short Name", max_length=10)
