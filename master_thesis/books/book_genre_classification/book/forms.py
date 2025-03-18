from django import forms

class FileUploadForm(forms.Form):
    file = forms.FileField(label='Upload Book File', required=True)

class BookGenreForm(forms.Form):
    file = forms.FileField()