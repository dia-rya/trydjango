from django.shortcuts import render

from .models import product

from .forms import productform, rawproductform

# control objects saved "product" app
def product_detail_view(request):
	obj = product.objects.get(id=1)
	# context = {
	# 	'title': obj.title,
	# 	'description': obj.description
	# }
	context = {
		'obj': obj
	}
	return render (request, "product/product_detail.html", context)

# Form 
# def product_create_view(request):
# 	form = productform(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 		# re-render to clear the form!
# 		form = productform()
# 	context = {
# 		'form': form
# 	}
# 	return render (request, "product/product_create.html", context)


def product_create_view(request):
	my_form = rawproductform()
	context = {
		"form": my_form
	}
	return render (request, "product/product_create.html", context)



# Data send through to change the title 
# def product_create_view(request):
# 	# print(request.POST)
# 	# print(request.GET)
# 	if request.method == "POST":
# 		# product.objects.create(title=my_new_title)
# 		my_new_title = request.POST.get('title')
# 		print (my_new_title)
# 	context = {}
# 	return render (request, "product/product_create.html", context)