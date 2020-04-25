from django.shortcuts import render
from .forms import DL3Form
from django.views.generic.edit import CreateView
from .models import KodPocztowy
from django.http import JsonResponse
import re

def kp(request):
	form_kp = DL3Form(request.POST)
	return render(request, 'dl3app/dl3.html', {'form_kp':form_kp})

def validate_kp(request):
	get_kod = request.GET.get('kodpocztowy', '0')
	input = re.match("([0-9]{2})(-)([0-9]{3})", get_kod)
	length = len(get_kod)
	if input is None:
		return JsonResponse({'is_valid' : 'falszywy'})
	data = { 'is_valid' : input[0], 'length' : length }
	return JsonResponse(data, safe=False)

