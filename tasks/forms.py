from django import forms
from matplotlib import widgets 
from . import models 
from lists import models as list_models
class CreateNewTask(forms.ModelForm):
    class Meta():
        model = models.Task
        fields = ('name','list')
        widgets = {
            'name':forms.TextInput(attrs={'class':'create-new-task'})
        }

    def __init__(self,*args,**kwargs):
        tuser = kwargs['initial']['user']
        super(CreateNewTask,self).__init__(*args,**kwargs)
        self.fields['list'].queryset = list_models.List.objects.filter(user=tuser)
        


            