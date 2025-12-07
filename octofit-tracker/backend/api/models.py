from django.db import models
from django.contrib.auth.models import User
from bson import ObjectId
import uuid


def generate_object_id():
    """Generate a MongoDB ObjectId"""
    return str(ObjectId())


class Team(models.Model):
    """Team model for group fitness activities"""
    _id = models.CharField(max_length=24, default=generate_object_id, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='led_teams')
    members = models.ManyToManyField(User, related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'teams'


class Activity(models.Model):
    """Activity model for logging exercises"""
    ACTIVITY_TYPES = [
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
        ('gym', 'Gym'),
        ('yoga', 'Yoga'),
        ('other', 'Other'),
    ]
    
    _id = models.CharField(max_length=24, default=generate_object_id, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    distance = models.FloatField(null=True, blank=True)  # in km
    duration = models.IntegerField()  # in minutes
    calories_burned = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.activity_type}"

    class Meta:
        db_table = 'activities'


class Workout(models.Model):
    """Workout program model"""
    _id = models.CharField(max_length=24, default=generate_object_id, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    target_type = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=20, default='intermediate')
    duration_weeks = models.IntegerField(default=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'workouts'


class Leaderboard(models.Model):
    """Leaderboard model for competitive tracking"""
    _id = models.CharField(max_length=24, default=generate_object_id, primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboards')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboards')
    rank = models.IntegerField()
    points = models.IntegerField(default=0)
    activities_count = models.IntegerField(default=0)
    total_distance = models.FloatField(default=0.0)
    total_calories = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.team} (Rank: {self.rank})"

    class Meta:
        db_table = 'leaderboards'
