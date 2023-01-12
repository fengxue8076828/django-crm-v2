from django.contrib.auth.forms import UserCreationForm,UsernameField
from django import forms
from .models import *

class CustomedUserCreationForm(UserCreationForm):
        class Meta:
            model = User
            fields = ("username",)
            field_classes = {"username": UsernameField}

class LeadForm(forms.ModelForm):
    class Meta:
        model=Lead
        fields={
            "first_name",
            "last_name",
            "age",
            "email",
            "image",
        }

class AssignAgentForm(forms.Form):
    agent=forms.ModelChoiceField(queryset=Agent.objects.none())

    def __init__(self,*args,**kwargs):
        request=kwargs.pop("request")
        agents=Agent.objects.filter(organizer=request.user.organizer)
        super().__init__(*args,**kwargs)
        self.fields["agent"].queryset=agents
        
         