from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Textarea, DateInput, Select
from service.models import Service


class TaskForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'company_name',
            'contact_name',
            'agent_name',
            'phone',
            'email',
            'task_name',
            'task_description',
            'start_date',
            'end_date',
            'active',
            'select_delivery',
            'select_status'
        ]

        widgets = {
            'company_name': TextInput(attrs={'placeholder': 'Please enter clients name', 'class': 'form-control'}),
            'contact_name': TextInput(attrs={'placeholder': 'Please enter clients contact person name',
                                             'class': 'form-control'}),
            'agent_name': Select(attrs={'class': 'form-select'}),
            'phone': NumberInput(attrs={'placeholder': 'Please enter contact phone number', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter clients email',  'class': 'form-control'}),
            'task_name': TextInput(attrs={'placeholder': 'Please enter service problem', 'class': 'form-control'}),
            'task_description': Textarea(attrs={'placeholder': 'Please enter detailed service problem',
                                                'class': 'form-control', 'rows': 5}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'select_status': Select(attrs={'class': 'form-select'}),
            'select_delivery': Select(attrs={'class': 'form-select'}),
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        get_email = cleaned_data['email']
        check_emails = Service.objects.filter(email=get_email)
        if check_emails:
            msg = 'Exista deja'
            self._errors['email'] = self.error_class([msg])

        get_date1 = cleaned_data['start_date']
        get_date2 = cleaned_data['end_date']

        if get_date1 > get_date2:
            msg2 = "Nu se poate ca data de inceput sa fie mai mare ca data de sfarsit"
            self._errors['end_date'] = self.error_class([msg2])

        return cleaned_data


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Service
#        fields = '__all__'
        fields = ['company_name', 'contact_name', 'agent_name', 'phone', 'email', 'task_description', 'task_asses', 'task_resolve', 'end_date', 'complete']

        widgets = {
            'company_name': TextInput(attrs={'placeholder': 'Please enter clients name', 'class': 'form-control'}),
            'contact_name': TextInput(attrs={'placeholder': 'Please enter clients contact person name', 'class': 'form-control'}),
            'agent_name': Select(attrs={'class': 'form-select'}),
            'phone': NumberInput(attrs={'placeholder': 'Please enter contact phone number', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter clients email',  'class': 'form-control'}),
            'task_description': Textarea(attrs={'placeholder': 'Please enter service problem', 'class': 'form-control',
                                         'rows': 5}),
            'task_asses': Textarea(attrs={'placeholder': 'Please enter detailed service solution', 'class': 'form-control',
                                   'rows': 5}),
            'task_resolve': Textarea(attrs={'placeholder': 'Please enter detailed service solution', 'class': 'form-control',
                                     'rows': 5}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'select_status': Select(attrs={'class': 'form-select'}),

        }
