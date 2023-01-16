from django import forms  
from projects.models import Projects
from django.forms import fields

class ProjectsForm(forms.ModelForm):  
    class Meta:  
        model = Projects  
        fields = "__all__"  