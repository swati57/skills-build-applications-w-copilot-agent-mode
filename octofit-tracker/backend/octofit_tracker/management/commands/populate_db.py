from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating test users...')
        user1 = User.objects.create(username='john_doe', email='john@example.com', password='password123')
        user2 = User.objects.create(username='jane_doe', email='jane@example.com', password='password123')

        self.stdout.write('Creating test teams...')
        team1 = Team.objects.create(name='Team Alpha')
        team1.members = [user1.id, user2.id]  # Store user IDs in the JSONField
        team1.save()

        self.stdout.write('Creating test activities...')
        Activity.objects.create(user=user1, activity_type='Running', duration='00:30:00')
        Activity.objects.create(user=user2, activity_type='Cycling', duration='01:00:00')

        self.stdout.write('Creating test leaderboard entries...')
        Leaderboard.objects.create(user=user1, score=100)
        Leaderboard.objects.create(user=user2, score=150)

        self.stdout.write('Creating test workouts...')
        Workout.objects.create(name='Morning Yoga', description='A relaxing morning yoga session.')
        Workout.objects.create(name='HIIT', description='High-intensity interval training.')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
