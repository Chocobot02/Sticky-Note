from django import forms
from .models import todolist
from django.forms import ModelForm


# class AddToDo(forms.Form):
#     todo = forms.CharField(label='ToDo:',
#                            max_length=100,
#                            required=False,
#                            widget=forms.TextInput(attrs={'class':'form-control'})
#                            )
#     priority = forms.BooleanField(label='is this important?',
#                                   required=False,
#                                   widget=forms.CheckboxInput()
#                                 )
class AddToDo(ModelForm):
    class Meta:
        model = todolist
        fields = ['todo', 'priority'] # or i can use "__all__" if all

        labels = {
            'todo':'Todo',
            'priority': 'is this important?'
        }

        widgets = {
            'todo': forms.TextInput(attrs={'class':'form-control'}),
        }

        # error_messages = {
        # }

