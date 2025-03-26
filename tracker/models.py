from django.db import models
from django.contrib.auth.models import User

FREQUENCY_CHOICES = [
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
]

class Medicine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, default='daily')
    dose_count = models.PositiveIntegerField(default=1)
    start_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.dosage})"
    
    def get_doses_taken(self, date):
        """Get number of doses taken for a specific date"""
        log = MedicineLog.objects.filter(
            user=self.user,
            medicine=self,
            date=date
        ).first()
        return log.taken if log else 0

class MedicineLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    date = models.DateField()
    taken = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('user', 'medicine', 'date')
        
    @classmethod
    def get_weekly_logs(cls, user, start_date):
        """Get logs for a week starting from start_date"""
        from datetime import timedelta
        end_date = start_date + timedelta(days=6)
        return cls.objects.filter(
            user=user,
            date__gte=start_date,
            date__lte=end_date
        ).order_by('date', 'medicine__name')
    
    @classmethod
    def get_monthly_logs(cls, user, year, month):
        """Get logs for a specific month"""
        return cls.objects.filter(
            user=user,
            date__year=year,
            date__month=month
        ).order_by('date', 'medicine__name')
    
    def is_complete(self):
        """Check if all doses for this medicine on this date are taken"""
        return self.taken >= self.medicine.dose_count
