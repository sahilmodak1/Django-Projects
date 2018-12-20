from django.shortcuts import render
from .models import Job
# Create your views here.
def home(request):
	all_jobs = Job.objects
	return render(request, 'jobs/home.html', {'all_jobs':all_jobs})
