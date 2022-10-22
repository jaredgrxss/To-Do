from django import forms 
from . import models 

class CreateNewList(forms.ModelForm):
    class Meta():
        model = models.List
        fields = ('name','description')

        widgets = {
            'name':forms.TextInput(attrs={'class':'create-list-name'}),
            'description':forms.Textarea(attrs={'class':'create-list-description'}),
        }