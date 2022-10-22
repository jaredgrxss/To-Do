from django import forms
from matplotlib import widgets 
from . import models 

class CreateNewTask(forms.ModelForm):
    class Meta():
        model = models.Task
        fields = ('name','list')

        widgets = {
            'name':forms.TextInput(attrs={'class':'create-new-task'})
        }