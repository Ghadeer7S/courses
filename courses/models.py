from django.contrib import admin
from django.db import models
from django.conf import settings

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.user.email
    
    @admin.display()
    def email(self):
        return self.user.email
    

class Podcast(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="podcasts/images/", blank=True, null=True)
    
    def __str__(self):
        return self.title


class Episode(models.Model):
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name='episodes')
    title = models.CharField(max_length=255)
    audio = models.FileField(upload_to="podcasts/audio/", blank=True, null=True)
    pdf = models.FileField(upload_to="podcasts/pdf/", blank=True, null=True) 
    notes = models.TextField(blank=True, null=True)
    notes_pdf = models.FileField(upload_to="podcasts/notes/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.podcast.title} - {self.title}"


class Script(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name='script')
    speaker = models.CharField(max_length=255)
    text = models.TextField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    
    def __str__(self):
        return f"{self.speaker} - {self.time_start}"
    
class Vocabulary(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name='vocabulary')
    word = models.CharField(max_length=255)
    meaning = models.TextField()
    
    def __str__(self):
        return self.word