from django import forms
# imports user model being used in project
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Lead, User, Agent

User = get_user_model()

class LeadModelForm(forms.ModelForm):
  class Meta:
    model = Lead
    fields = (
      'first_name',
      'last_name',
      'age',
      'agent'
    )

class LeadForm(forms.Form):
  first_name = forms.CharField()
  last_name = forms.CharField()
  age = forms.IntegerField(min_value=0)
  
class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username',]
    field_classes = {'username': UsernameField}
    
class AssignAgentForm(forms.Form):
  agent = forms.ModelChoiceField(queryset=Agent.objects.none())
  
  # override __init__ method in order to override the queryset defined above dynamically
  def __init__(self, *args, **kwargs):
    # remove the element from the args because django's forms will not be expecting that argument
    request = kwargs.pop('request')
    user = request.user
    agents = Agent.objects.filter(organisation=user.userprofile)
    super(AssignAgentForm, self).__init__(*args, **kwargs)
    # override form's agent field queryset after form has been initialized above
    self.fields['agent'].queryset = agents
    
  class LeadCategoryUpdateForm(forms.ModelForm):
    class Meta:
      model = Lead
      fields = (
        'category'
      )