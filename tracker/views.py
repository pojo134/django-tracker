from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Medicine, MedicineLog
from .forms import MedicineForm
from datetime import date

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
    
    # Get all logs for today
    logs = MedicineLog.objects.filter(user=request.user, date=today)
    
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
    }
    return render(request, 'tracker/medicine_log.html', context)

@login_required
def mark_taken(request, log_id):
    log = get_object_or_404(MedicineLog, id=log_id, user=request.user)
    log.taken = True
    log.save()
    messages.success(request, f'Marked {log.medicine.name} as taken!')
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
    messages.success(request, f'Medicine {medicine.name} deactivated!')
    return redirect('medicine_log')
