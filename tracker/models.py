from django.db import models
from django.contrib.auth.models import User

class MedicineLog(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicitly define the primary key
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    taken = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'date')
