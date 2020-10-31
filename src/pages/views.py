from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	print (args, kwargs)
	print (request.user)
	# return HttpResponse("<h1>Hello World</h1>")
	return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
	my_context = {
		"title": "this is about us",
		"this_is_true": True,
		"my_number": 123,
		"my_list": [1313, 4231, 312, "aasd"],
		"my_html": "<h1>Hello Cooolies</h1>"
	}
	return render(request, "about.html", my_context)

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})

