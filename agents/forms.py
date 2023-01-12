from django.forms import ModelForm
from leads.models import Agent

class AgentForm(ModelForm):
    class Meta:
        model=Agent
        fields={
            'user',
            'image',
        }
