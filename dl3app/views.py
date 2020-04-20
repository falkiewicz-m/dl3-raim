from django.shortcuts import render
# from .forms import DL3Form
from django.views.generic.edit import CreateView

# class DL3View(CreateView):
# 	template_name = 'dl3.html'
# 	form_class = DL3Form

def post_l(request):
	return render(request, 'dl3app/dl3.html', {})

# Create your views here.
