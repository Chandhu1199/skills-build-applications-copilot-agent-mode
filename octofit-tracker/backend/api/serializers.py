from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Team, Activity, Workout, Leaderboard


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']


class TeamSerializer(serializers.ModelSerializer):
    """Serializer for Team model"""
    leader = UserSerializer(read_only=True)
    members = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = Team
        fields = ['_id', 'name', 'description', 'leader', 'members', 'created_at', 'updated_at']
        read_only_fields = ['_id', 'created_at', 'updated_at']


class ActivitySerializer(serializers.ModelSerializer):
    """Serializer for Activity model"""
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Activity
        fields = ['_id', 'user', 'activity_type', 'distance', 'duration', 'calories_burned', 'description', 'created_at', 'updated_at']
        read_only_fields = ['_id', 'created_at', 'updated_at']


class WorkoutSerializer(serializers.ModelSerializer):
    """Serializer for Workout model"""
    created_by = UserSerializer(read_only=True)
    
    class Meta:
        model = Workout
        fields = ['_id', 'name', 'description', 'created_by', 'target_type', 'difficulty', 'duration_weeks', 'created_at', 'updated_at']
        read_only_fields = ['_id', 'created_at', 'updated_at']


class LeaderboardSerializer(serializers.ModelSerializer):
    """Serializer for Leaderboard model"""
    user = UserSerializer(read_only=True)
    team = TeamSerializer(read_only=True)
    
    class Meta:
        model = Leaderboard
        fields = ['_id', 'team', 'user', 'rank', 'points', 'activities_count', 'total_distance', 'total_calories', 'updated_at']
        read_only_fields = ['_id', 'updated_at']
