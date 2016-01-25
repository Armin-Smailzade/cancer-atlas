from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

def index(request):

	

	return render(request, 'map/index.html', 
		{}
		)
