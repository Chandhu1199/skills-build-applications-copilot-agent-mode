from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from api.models import Team, Activity, Workout, Leaderboard


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Create test users
        self.stdout.write('Creating test users...')
        users = []
        user_names = ['alice', 'bob', 'charlie', 'diana', 'eve']
        for name in user_names:
            user, created = User.objects.get_or_create(
                username=name,
                defaults={
                    'email': f'{name}@example.com',
                    'first_name': name.capitalize(),
                    'last_name': 'Fitness'
                }
            )
            if created:
                user.set_password('password123')
                user.save()
            users.append(user)
        self.stdout.write(self.style.SUCCESS(f'Created {len(users)} users'))

        # Create test teams
        self.stdout.write('Creating test teams...')
        teams = []
        team_names = ['Fitness Warriors', 'Running Club', 'Gym Buddies']
        for i, team_name in enumerate(team_names):
            team, created = Team.objects.get_or_create(
                name=team_name,
                defaults={
                    'description': f'{team_name} team description',
                    'leader': users[i % len(users)]
                }
            )
            teams.append(team)
            if created:
                team.members.add(*users[:i+2])
        self.stdout.write(self.style.SUCCESS(f'Created {len(teams)} teams'))

        # Create test activities
        self.stdout.write('Creating test activities...')
        activity_types = ['running', 'cycling', 'swimming', 'gym', 'yoga']
        activities_created = 0
        for user in users:
            for i, activity_type in enumerate(activity_types):
                activity, created = Activity.objects.get_or_create(
                    user=user,
                    activity_type=activity_type,
                    defaults={
                        'distance': 5.0 + i,
                        'duration': 30 + (i * 10),
                        'calories_burned': 300 + (i * 50),
                        'description': f'{activity_type} activity for {user.username}'
                    }
                )
                if created:
                    activities_created += 1
        self.stdout.write(self.style.SUCCESS(f'Created {activities_created} activities'))

        # Create test workouts
        self.stdout.write('Creating test workouts...')
        workouts = []
        workout_names = ['HIIT Training', 'Yoga Flow', 'Strength Training']
        for i, workout_name in enumerate(workout_names):
            workout, created = Workout.objects.get_or_create(
                name=workout_name,
                defaults={
                    'description': f'{workout_name} program',
                    'created_by': users[i % len(users)],
                    'target_type': ['cardio', 'flexibility', 'strength'][i],
                    'difficulty': ['beginner', 'intermediate', 'advanced'][i],
                    'duration_weeks': 4 + (i * 2)
                }
            )
            workouts.append(workout)
        self.stdout.write(self.style.SUCCESS(f'Created {len(workouts)} workouts'))

        # Create test leaderboards
        self.stdout.write('Creating test leaderboards...')
        leaderboards_created = 0
        for team in teams:
            for rank, user in enumerate(users[:3], 1):
                leaderboard, created = Leaderboard.objects.get_or_create(
                    team=team,
                    user=user,
                    defaults={
                        'rank': rank,
                        'points': 1000 - (rank * 100),
                        'activities_count': 10 - (rank * 2),
                        'total_distance': 50.0 - (rank * 5),
                        'total_calories': 5000 - (rank * 500)
                    }
                )
                if created:
                    leaderboards_created += 1
        self.stdout.write(self.style.SUCCESS(f'Created {leaderboards_created} leaderboards'))

        self.stdout.write(self.style.SUCCESS('Database population completed successfully!'))
