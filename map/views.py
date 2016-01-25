from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

def index(request):

	return render(request, 'map/landing/index.html', 
		{}
		)

def map(request):

	return render(request, 'map/visuals/map.html', 
		{}
		)

def chart(request):

	return render(request, 'map/visuals/chart.html', 
		{}
		)