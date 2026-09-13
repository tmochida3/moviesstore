from django.contrib import admin
from .models import Movie, Review

class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']

admin.site.register(Movie, MovieAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'movie', 'user', 'date', 'reported']
    list_filter = ['reported']
    search_fields = ['comment', 'movie__name', 'user__username']

admin.site.register(Review, ReviewAdmin)