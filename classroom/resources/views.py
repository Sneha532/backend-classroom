from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Resource, Schedule, Maintenance
import json
from datetime import datetime

def index(request):
    return render(request, 'index.html')

def get_resources(request):
    resources = Resource.objects.all()
    resources_list = [{'id': r.id, 'name': r.name, 'type': r.type} for r in resources]
    return JsonResponse(resources_list, safe=False)

@csrf_exempt
def add_schedule(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        schedule = Schedule(
            resource_id=data['resource_id'],
            start_time=datetime.strptime(data['start_time'], '%Y-%m-%dT%H:%M:%S'),
            end_time=datetime.strptime(data['end_time'], '%Y-%m-%dT%H:%M:%S'),
            booked_by=data['booked_by']
        )
        schedule.save()
        return JsonResponse({'message': 'Schedule added successfully!'})

@csrf_exempt
def add_maintenance(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        maintenance = Maintenance(
            resource_id=data['resource_id'],
            maintenance_date=datetime.strptime(data['maintenance_date'], '%Y-%m-%dT%H:%M:%S'),
            description=data['description']
        )
        maintenance.save()
        return JsonResponse({'message': 'Maintenance record added successfully!'})