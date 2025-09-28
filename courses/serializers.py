from rest_framework import serializers
from .models import Podcast, Script, Student, Episode, Vocabulary

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'phone', 'address', 'birth_date']
        
class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = ['id', 'title', 'description', 'category', 'image']
 
 
class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Script
        fields = ['id', 'speaker', 'text', 'time_start', 'time_end']
        
class VocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = ['id', 'word', 'meaning']
        
class EpisodeSerializer(serializers.ModelSerializer):
    script = ScriptSerializer(many=True, read_only=True)
    vocabulary = VocabularySerializer(many=True, read_only=True)
    class Meta:
        model = Episode
        fields = ['id', 'title', 'audio', 'pdf', 'notes', 'notes_pdf', 'created_at', 'script', 'vocabulary']
        
