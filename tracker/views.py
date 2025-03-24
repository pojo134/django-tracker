from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MedicineLog
from datetime import date

@login_required
def medicine_log(request):
    today = date.today()
    log, created = MedicineLog.objects.get_or_create(user=request.user, date=today)
    if request.method == 'POST':
        log.taken = True
        log.save()
        return redirect('medicine_log')
    return render(request, 'tracker/medicine_log.html', {'log': log})
