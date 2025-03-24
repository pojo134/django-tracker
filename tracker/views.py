from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Medicine, MedicineLog
from .forms import MedicineForm
from datetime import date, datetime, timedelta
from django.utils import timezone
import calendar

@login_required
def medicine_log(request):
    today = date.today()
    user_medicines = Medicine.objects.filter(user=request.user, active=True)
    
    # Create medicine logs for today if they don't exist
    for medicine in user_medicines:
        MedicineLog.objects.get_or_create(
            user=request.user,
            medicine=medicine,
            date=today,
            defaults={'taken': False}
        )
    
    # Get all logs for today (only for active medicines)
    logs = MedicineLog.objects.filter(
        user=request.user, 
        date=today,
        medicine__active=True
    )
    
    # Handle adding new medicine
    if request.method == 'POST' and 'add_medicine' in request.POST:
        form = MedicineForm(request.POST)
        if form.is_valid():
            medicine = form.save(commit=False)
            medicine.user = request.user
            medicine.save()
            # Create log for the new medicine
            MedicineLog.objects.create(user=request.user, medicine=medicine, date=today)
            messages.success(request, f'Medicine {medicine.name} added successfully!')
            return redirect('medicine_log')
    else:
        form = MedicineForm()
    
    context = {
        'logs': logs,
        'form': form,
        'today': today,
        'view_type': 'daily'
    }
    return render(request, 'tracker/medicine_log.html', context)

@login_required
def weekly_log(request):
    today = date.today()
    # Get the start of the week (Monday)
    start_date = today - timedelta(days=today.weekday())
    
    # Get all active medicines
    user_medicines = Medicine.objects.filter(user=request.user, active=True)
    
    # Group logs by date
    grouped_logs = {}
    for i in range(7):
        current_date = start_date + timedelta(days=i)
        
        # Create logs for medicines that don't have one for this date
        for medicine in user_medicines:
            MedicineLog.objects.get_or_create(
                user=request.user,
                medicine=medicine,
                date=current_date,
                defaults={'taken': False}
            )
        
        # Get logs for this date
        day_logs = MedicineLog.objects.filter(
            user=request.user,
            date=current_date,
            medicine__active=True  # Only include active medicines
        )
        
        grouped_logs[current_date] = day_logs
    
    context = {
        'grouped_logs': grouped_logs,
        'start_date': start_date,
        'end_date': start_date + timedelta(days=6),
        'view_type': 'weekly'
    }
    return render(request, 'tracker/medicine_log.html', context)

@login_required
def monthly_log(request):
    today = date.today()
    year = today.year
    month = today.month
    
    # Get all active medicines
    user_medicines = Medicine.objects.filter(user=request.user, active=True)
    
    # Get the number of days in the month
    _, num_days = calendar.monthrange(year, month)
    
    # Group logs by date
    grouped_logs = {}
    for day in range(1, num_days + 1):
        current_date = date(year, month, day)
        
        # Only create logs for dates up to today
        if current_date <= today:
            # Create logs for medicines that don't have one for this date
            for medicine in user_medicines:
                MedicineLog.objects.get_or_create(
                    user=request.user,
                    medicine=medicine,
                    date=current_date,
                    defaults={'taken': False}
                )
            
            # Get logs for this date (only active medicines)
            day_logs = MedicineLog.objects.filter(
                user=request.user,
                date=current_date,
                medicine__active=True
            )
            
            grouped_logs[current_date] = day_logs
    
    context = {
        'grouped_logs': grouped_logs,
        'month_name': calendar.month_name[month],
        'year': year,
        'view_type': 'monthly'
    }
    return render(request, 'tracker/medicine_log.html', context)

@login_required
def mark_taken(request, log_id):
    log = get_object_or_404(MedicineLog, id=log_id, user=request.user)
    log.taken = True
    log.save()
    messages.success(request, f'Marked {log.medicine.name} as taken!')
    
    # Determine which view to redirect to based on the referer
    referer = request.META.get('HTTP_REFERER', '')
    if 'weekly' in referer:
        return redirect('weekly_log')
    elif 'monthly' in referer:
        return redirect('monthly_log')
    else:
        return redirect('medicine_log')

@login_required
def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            medicine = form.save(commit=False)
            medicine.user = request.user
            medicine.save()
            messages.success(request, f'Medicine {medicine.name} added successfully!')
            return redirect('medicine_log')
    else:
        form = MedicineForm()
    return render(request, 'tracker/add_medicine.html', {'form': form})

@login_required
def deactivate_medicine(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id, user=request.user)
    medicine.active = False
    medicine.save()
    
    # Also remove any logs for today for this medicine
    today = date.today()
    MedicineLog.objects.filter(user=request.user, medicine=medicine, date=today).delete()
    
    messages.success(request, f'Medicine {medicine.name} deactivated!')
    
    # Determine which view to redirect to based on the referer
    referer = request.META.get('HTTP_REFERER', '')
    if 'weekly' in referer:
        return redirect('weekly_log')
    elif 'monthly' in referer:
        return redirect('monthly_log')
    else:
        return redirect('medicine_log')
