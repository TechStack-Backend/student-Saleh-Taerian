from django import forms
from .models import Developer

class developer_login(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    age = forms.IntegerField()
    
    
class add_project(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)
    developers = forms.ModelMultipleChoiceField(queryset=Developer.objects.all() , widget = forms.CheckboxSelectMultiple)
    
    
class add_skill(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)
    developer  = forms.ModelChoiceField(queryset= Developer.objects.all())
    