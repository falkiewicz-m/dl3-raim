from django.shortcuts import render
from .forms import DL3Form
from django.views.generic.edit import CreateView
from .models import KodPocztowy
from django.http import JsonResponse
import re

# class DL3View(CreateView):
# 	template_name = 'dl3.html'
# 	form_class = DL3Form

def post_l(request):
	return render(request, 'dl3app/dl3.html', {})

# Create your views here.
def kp(request):
	form_kp = DL3Form(request.POST)
	return render(request, 'dl3app/dl3.html', {'form_kp':form_kp})

def validate_kp(request):
	get_kod = request.GET.get('kodpocztowy', '0')
	data = {
		'is_valid' : re.match("([0-9]{2})(-)([0-9]{3})", get_kod)
	}
	return JsonResponse(data)

