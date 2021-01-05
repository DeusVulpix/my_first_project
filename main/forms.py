from .models import Tasks, fight_tab, user_stats
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ["title", "task"]
        widgets = {
            "title": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input task name'
            }),
            "task": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Input dicription'
            }),
        }
class fight_tab_form(forms.ModelForm):
    class Meta:
        model = fight_tab
        fields = [
            'choice_is',
            'yours',
            'dont_be_late'
        ]
class rawform(forms.Form):
    title       = forms.CharField()
    desctiption = forms.CharField()

class user_statts(forms.ModelForm):
    class Meta:
        model = user_stats
        fields = [
            'user_name',
            'hp',
            'damage'
        ]
        widgets = {
            "user_name": forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Input task name'
            }),
            "hp": forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Input task name'
            }),
            "damage": forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Input task name'
            })
        }
