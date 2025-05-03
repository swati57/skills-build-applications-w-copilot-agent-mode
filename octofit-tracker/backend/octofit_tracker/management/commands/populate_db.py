from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta
from django.db import connection
import os

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Debug: Verifying database connection...')
        self.stdout.write(f'Database connection: {connection.settings_dict}')

        self.stdout.write('Debug: Checking script environment...')
        self.stdout.write(f'Python executable: {os.sys.executable}')
        self.stdout.write(f'Environment variables: {os.environ}')

        self.stdout.write('Debug: Starting database population...')
        try:
            self.stdout.write('Debug: Creating test users...')
            user1 = User.objects.create(username='john_doe', email='john@example.com', password='password123')
            user2 = User.objects.create(username='jane_doe', email='jane@example.com', password='password123')
        except Exception as e:
            self.stderr.write(f'Error creating users: {e}')

        try:
            self.stdout.write('Debug: Creating test teams...')
            team1 = Team.objects.create(name='Team Alpha')
            team1.members = [{'username': user1.username, 'email': user1.email}, {'username': user2.username, 'email': user2.email}]  # Ensure valid JSON-compatible structure
            team1.save()
        except Exception as e:
            self.stderr.write(f'Error creating teams: {e}')

        try:
            self.stdout.write('Debug: Creating test activities...')
            Activity.objects.create(user=user1, activity_type='Running', duration='00:30:00')
            Activity.objects.create(user=user2, activity_type='Cycling', duration='01:00:00')
        except Exception as e:
            self.stderr.write(f'Error creating activities: {e}')

        try:
            self.stdout.write('Debug: Creating test leaderboard entries...')
            Leaderboard.objects.create(user=user1, score=100)
            Leaderboard.objects.create(user=user2, score=150)
        except Exception as e:
            self.stderr.write(f'Error creating leaderboard entries: {e}')

        try:
            self.stdout.write('Debug: Creating test workouts...')
            Workout.objects.create(name='Morning Yoga', description='A relaxing morning yoga session.')
            Workout.objects.create(name='HIIT', description='High-intensity interval training.')
        except Exception as e:
            self.stderr.write(f'Error creating workouts: {e}')

        self.stdout.write(self.style.SUCCESS('Debug: Successfully populated the database with test data.'))
