from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank =True) #NULL by default is false, this is not a required field.
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank = True)
    tags = models.ManyToManyField('Tag', blank= True)
    vote_total = models.IntegerField(default=0, null=True, blank =True)
    vote_ratio = models.IntegerField(default=0, null = True, blank = True)
    created = models.DateTimeField(auto_now_add=True) #Timestamp and Datae, and also add manually, but this will add automatically
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_TYPE = (('up', 'Up Vote'), ('down', 'Down Vote'))
    #owner
    project = models.ForeignKey(Project, on_delete=models.CASCADE) #Delete all reviews if project is deleted
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE) #This will be drop down list
    created = models.DateTimeField(auto_now_add=True) #Timestamp and Datae, and also add manually, but this will add automatically
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True) #Timestamp and Datae, and also add manually, but this will add automatically
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    #Creating many to many
    def __str__(self):
        return self.name
    
    
    
