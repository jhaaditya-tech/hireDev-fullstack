
from .models import Project #Importing the Project Class
from django import forms
from django.forms import ModelForm, widgets

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'demo_link', 'source_link','tags','featured_image' ]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
        
    #Adding classes by overwriting the init file
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
            
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
        # self.fields['title'].widget.attrs.update({'class':'input', 'placeholder':'Add title'})
        
    