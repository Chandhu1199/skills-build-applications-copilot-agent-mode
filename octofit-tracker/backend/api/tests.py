from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Workout, Leaderboard


class UserTestCase(TestCase):
    """Test cases for User model"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_user_creation(self):
        """Test user creation"""
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')


class TeamTestCase(TestCase):
    """Test cases for Team model"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='teamleader',
            email='leader@example.com',
            password='testpass123'
        )
        self.team = Team.objects.create(
            name='Fitness Warriors',
            description='A team of fitness enthusiasts',
            leader=self.user
        )

    def test_team_creation(self):
        """Test team creation"""
        self.assertEqual(self.team.name, 'Fitness Warriors')
        self.assertEqual(self.team.leader, self.user)


class ActivityTestCase(TestCase):
    """Test cases for Activity model"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='runner',
            email='runner@example.com',
            password='testpass123'
        )
        self.activity = Activity.objects.create(
            user=self.user,
            activity_type='running',
            distance=5.0,
            duration=30,
            calories_burned=300
        )

    def test_activity_creation(self):
        """Test activity creation"""
        self.assertEqual(self.activity.activity_type, 'running')
        self.assertEqual(self.activity.distance, 5.0)


class WorkoutTestCase(TestCase):
    """Test cases for Workout model"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='trainer',
            email='trainer@example.com',
            password='testpass123'
        )
        self.workout = Workout.objects.create(
            name='HIIT Training',
            description='High Intensity Interval Training',
            created_by=self.user,
            target_type='cardio',
            difficulty='advanced'
        )

    def test_workout_creation(self):
        """Test workout creation"""
        self.assertEqual(self.workout.name, 'HIIT Training')
        self.assertEqual(self.workout.created_by, self.user)
