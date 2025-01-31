from django import forms
from .models import Day,Todo

class IndexForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = ['day']
        widgets = {
            'day':forms.DateInput(attrs={'type':'date'})
            } 
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['selected_day', 'assignments', 'is_done']
        widgets = {
            'selected_day': forms.Select(), 
            'assignments': forms.TextInput(attrs={'placeholder': 'タスクを入力してください'}),
            'is_done': forms.CheckboxInput(), 
        }

        


    