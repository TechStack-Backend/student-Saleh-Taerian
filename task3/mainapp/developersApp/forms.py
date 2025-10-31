from django import forms
from .models import Developer
from django.forms import ModelForm
from .models import Developer, Skill, Project


class developer_login(ModelForm):
    class Meta:
        model = Developer
        fields = ["first_name", "last_name", "email", "age"]

    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age < 18:
            raise forms.ValidationError("age must not be under 18")
        return age


# class developer_login(forms.Form):
#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     email = forms.CharField(max_length=100)
#     age = forms.IntegerField()


class add_project(ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "developers"]
        widgets = {"developers": forms.CheckboxSelectMultiple()}

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if len(description) == 0:
            raise forms.ValidationError("description must not be empty")
        return description


# class add_project(forms.Form):
#     title = forms.CharField(max_length=100)
#     description = forms.CharField(max_length=100)
#     developers = forms.ModelMultipleChoiceField(queryset=Developer.objects.all() , widget = forms.CheckboxSelectMultiple)


class add_skill(ModelForm):
    class Meta:
        model = Skill
        fields = ["title", "description", "developer"]

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if len(description) == 0:
            raise forms.ValidationError("description must not be empty")
        return description

# class add_skill(forms.Form):
#     title = forms.CharField(max_length=100)
#     description = forms.CharField(max_length=100)
#     developer  = forms.ModelChoiceField(queryset= Developer.objects.all())
