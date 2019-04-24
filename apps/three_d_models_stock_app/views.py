from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
	return render(request, 'three_d_models_stock_app/index.html')

def login(request):
	return render(request, 'three_d_models_stock_app/login.html')

def registration(request):
	return render(request, 'three_d_models_stock_app/registration.html')

def user_page(request, id):
	context = {
		"users": User.objects.filter(id=id)
	}
	return render(request, 'three_d_models_stock_app/user_page.html', context)

def add_new_model(request):
	if request.method == "POST":
		title = request.POST['title']
		category = request.POST['category']
		format = request.POST['format']
		description = request.POST['description']
		tag = request.POST['tag']
		cover = request.POST['cover']
		link = request.POST['link']
		Model.objects.create(title='title', 
						  category='category', 
					   description='description', 
					   		format='format', 
					   		   tag='tag', 
					   		 cover='cover', 
					   		  link='link')

		return redirect(request, '/user_page')

def new_model_page(request):

	return render(request, 'three_d_models_stock_app/new_model_page.html')

def model_page(request):
	return render(request, 'three_d_models_stock_app/model_page.html')