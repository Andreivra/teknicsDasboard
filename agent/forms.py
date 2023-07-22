from django import forms
from django.forms import TextInput, EmailInput
from agent.models import Agent


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
        }


class AgentUpdateForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
        }
