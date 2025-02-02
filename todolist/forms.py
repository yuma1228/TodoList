from django import forms
from .models import Day,Todo
from django.core.exceptions import ValidationError
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
        
    def clean_assignments(self):
            selected_day = self.cleaned_data['selected_day']
            assignments  = self.cleaned_data['assignments']
            if Todo.objects.filter(selected_day=selected_day,assignments=assignments).exists():
                raise ValidationError('同じタスクが既に存在します。')
            return self.cleaned_data

        


    