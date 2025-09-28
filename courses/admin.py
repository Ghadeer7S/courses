from django.contrib import admin
from .models import Student, Podcast, Episode, Script, Vocabulary

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['email', 'phone', 'address', 'birth_date']

@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    search_fields = ['title', 'category']
    list_filter = ['category']
    
class ScriptInline(admin.TabularInline):
    model = Script
    fields = ['speaker', 'time_start', 'time_end', 'text']
    extra = 1
    
class VocabularyInline(admin.TabularInline):
    model = Vocabulary
    fields = ['word', 'meaning']
    extra = 1

@admin.register(Episode)    
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ['title', 'podcast', 'created_at']
    list_filter = ['podcast']
    list_select_related = ['podcast']
    search_fields = ['title', 'podcast__title']
    inlines = [ScriptInline, VocabularyInline]