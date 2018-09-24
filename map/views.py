from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.urls import reverse
from .models import Location as LocationModel
from django.template import RequestContext, loader
from .forms import LocationForm

import json
class HomePage(View):
	def get(self, request):
		return render(request, "index.html")

class Location(View):
	def get(self, request):
		locations = LocationModel.objects.all()
		temp_location_array = [location.serialize for location in locations]
		
		for locations in temp_location_array:
			obj = LocationModel.objects.filter(lat=float(locations['lat'])).get(lng=float(locations['lng']))

		return HttpResponse(json.dumps(temp_location_array), content_type="application/json")

class AddLocation(View):
	def get(self, request):
		form = LocationForm()
		template = "location_form.html"
		return render(request, template, {'form':form})

	def post(self, request):
		bound_form = LocationForm(request.POST)
		template = "location_form.html"
		if bound_form.is_valid():
			bound_form.save()
			return HttpResponse(json.dumps({"result":"success"}))
		else:
			bound_form = LocationForm(request.POST)
			print("fail")
			print(render(request, template, {'form':bound_form}))
			template = "location_form.html"
			return render(request, template, {'form':bound_form})