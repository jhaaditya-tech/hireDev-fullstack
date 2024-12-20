from django.forms import ModelForm
from .models import Project #Importing the Project Class

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'demo_link', 'source_link','tags' ]