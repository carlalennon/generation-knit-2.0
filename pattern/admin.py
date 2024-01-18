from django.contrib import admin
from .models import Pattern
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Pattern)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', )
    search_fields = ['title']
    summernote_fields = ('content',)
# Register your models here.
