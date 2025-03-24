from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, timedelta
from tracker.models import Medicine, MedicineLog
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Reset medicine logs for a new day'

    def handle(self, *args, **options):
        today = date.today()
        
        # Get all active users
        users = User.objects.all()
        
        for user in users:
            # Get all active medicines for the user
            medicines = Medicine.objects.filter(user=user, active=True)
            
            # Create new logs for today with taken=False
            for medicine in medicines:
                MedicineLog.objects.get_or_create(
                    user=user,
                    medicine=medicine,
                    date=today,
                    defaults={'taken': False}
                )
                
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created medicine logs for {today}')
        )
