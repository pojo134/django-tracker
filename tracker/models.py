from django.db import models
from django.contrib.auth.models import User

class Medicine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    start_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.dosage})"

class MedicineLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    date = models.DateField()
    taken = models.BooleanField(default=False)

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
