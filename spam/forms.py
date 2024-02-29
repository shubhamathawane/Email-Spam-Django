from django import forms

class EmailForm(forms.Form):
    email  = forms.CharField(label='Email Text',
        widget=forms.Textarea(attrs={'class': 'form-control border-0 p-3 rounded', 'style': 'height: 244px; width: 555px'}),
    )