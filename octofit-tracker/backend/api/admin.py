from django.contrib import admin
from .models import Team, Activity, Workout, Leaderboard


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'leader', 'created_at']
    search_fields = ['name', 'description']
    list_filter = ['created_at']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user', 'activity_type', 'duration', 'created_at']
    search_fields = ['user__username', 'activity_type']
    list_filter = ['activity_type', 'created_at']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_by', 'difficulty', 'created_at']
    search_fields = ['name', 'description']
    list_filter = ['difficulty', 'created_at']


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['user', 'team', 'rank', 'points']
    search_fields = ['user__username', 'team__name']
    list_filter = ['rank', 'updated_at']
