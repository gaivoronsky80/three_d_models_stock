from django.shortcuts import render, redirect, HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.db.models import Q
from .models import *
import bcrypt

# START PAGE

def index(request): 
	context = {
		"img_index": Model.objects.all().order_by('-created_at')
	}
	return render(request, 'three_d_models_stock_app/index.html', context)

# SEARCH BAR

def search(request):
	template = 'three_d_models_stock_app/search.html'
	query = request.GET.get('q')
	results = Model.objects.filter(Q(title__icontains=query) | Q(category__icontains=query))
	
	context = {
		'items': results,
	}
	return render(request, template, context)

# REGISTRATION

def register_process(request):
	errors = User.objects.registration_validator(request.POST)
	if(len(errors))>0:
		for key, value in errors.items():
			messages.error(request, value)
			return redirect('/register')
	else:
		firstName = request.POST.get('first_name')
		print(firstName)
		lastName = request.POST.get('last_name')
		email = request.POST.get('email')
		request.session['first_name'] = firstName
		request.session['email'] = email
		hashed_password = bcrypt.hashpw(request.POST.get('password').encode(),bcrypt.gensalt())
		user = User.objects.create(first_name=firstName, last_name=lastName, email=email,password=hashed_password)
		print (hashed_password)
		request.session['user_id'] = user.id
		return redirect ('/user_page')

# LOGIN

def login_process(request):
    errors = {}
    email = request.POST.get('email')
    pw = request.POST.get('password')
    if email == 'gaivoronsky80@gmail.com':
    	return redirect('/admin')
    if len(email) < 1:
        errors['email'] = "Email field cannot be blank"
    if len(pw) < 1:
            errors['password'] ='Password field cannot be blank'
    else:
        user = User.objects.filter(email=email)
        if user:
            user = User.objects.get(email=email)
            if  not bcrypt.checkpw(pw.encode(), user.password.encode()):
                errors['password'] = "Could not be logged in"
    if(len(errors)):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/login')
    else:
        request.session['user_id']= user.id
        return redirect ('/user_page')

# USER ADMIN PAGE

def user_page(request):
	id = request.session['user_id']
	current_user = User.objects.get(id=id)
	uploaded = Model.objects.filter(author_id=current_user).count(),
	context = {
		"users": User.objects.filter(id=id),
		"models": Model.objects.filter(author=current_user).order_by('-created_at'),
		"show_news": Model.objects.last(),
		"counts": uploaded
	}
	return render(request, 'three_d_models_stock_app/user_page.html', context)

# EDIT USER PRIFILE

def add_edit_user_page(request, id):
	id = request.session['user_id']
	firstName = request.POST['first_name']
	lastName = request.POST['last_name']
	email = request.POST['email']
	context = {
		"users": User.objects.filter(id=id).update(first_name=firstName, last_name=lastName, email=email)
	}
	return redirect('/user_page', context)

# DELETE USER PRIFILE

def delete_user_profile(request, id):
	id = request.session['user_id']
	context = {
		"users": User.objects.filter(id=id).delete()
	}
	return redirect('/index', context)


# UPLOAD NEW MODEL

def add_new_model(request):
	if request.method == "POST" and request.FILES['cover'] or request.FILES['link']:
		id = request.session['user_id']
		title = request.POST['title']
		category = request.POST['category']
		format = request.POST['format']
		description = request.POST['description']
		tag = request.POST['tag']
		cover = request.FILES['cover']
		link = request.FILES['link']
		fs = FileSystemStorage()
		filename = fs.save(cover.name, cover)
		filename = fs.save(link.name, link)
		uploaded_file_url = fs.url(filename)
		author = User.objects.get(id=id)
		Model.objects.create(title= title, 
						  category= category, 
					   description= description, 
					   		format= format, 
					   		   tag= tag, 
					   		 cover= cover, 
					   		  link= link,
					   		author= author)

		return redirect('/user_page', {'uploaded_file_url': uploaded_file_url})

# EDIT MODEL INFO

def add_update_model(request, id):
	if request.method == "POST":
		id = request.session['user_id']
		title = request.POST['title']
		category = request.POST['category']
		format = request.POST['format']
		description = request.POST['description']
		tag = request.POST['tag']
		cover = request.FILES['cover']
		link = request.FILES['link']
		fs = FileSystemStorage()
		filename = fs.save(cover.name, cover)
		filename = fs.save(link.name, link)
		uploaded_file_url = fs.url(filename)
		author = User.objects.get(id=id)
		context = {
			"models": Model.objects.get(id=id).update(title= title, 
												   category= category, 
												description= description, 
													 format= format, tag= tag, 
													  cover= cover, 
													   link= link, 
													 author= author)
		}

		return redirect('/user_page', {'uploaded_file_url': uploaded_file_url}, context)

# MODEL INFO

def model_info(request, id):
	context = {
		'info': Model.objects.filter(id=id)
	}
	return render(request, 'three_d_models_stock_app/model_info_page.html', context)

# CATEGORY PAGE

def category(request):
	if request.method == "POST":
		query = request.POST['category']

		context = {
			'items': Model.objects.filter(category=query)
		}
		return render(request, 'three_d_models_stock_app/category_page.html', context)

# HOME PAGE

def session_home(request):
	context = {
		"img_home": Model.objects.all().order_by('-created_at')
	}
	return render(request, 'three_d_models_stock_app/session_home.html', context)

# DELETE MODEL

def delete(request, id):
	context = {
		"models": Model.objects.filter(id=id).delete()
	}
	return redirect('/user_page', context)

# ADMIN ACCESS

def admin(request):
	uploaded_models = Model.objects.all().count(),
	registered_users = User.objects.all().count(),
	context = {
		"users": User.objects.all().order_by('-created_at'),
		"models": Model.objects.all().order_by('-created_at'),
		"count_users": registered_users,
		"count_models": uploaded_models
	}
	return render(request, 'three_d_models_stock_app/admin_page.html', context)

def admin_control(request, id):
	context = {
		"models": Model.objects.filter(id=id).delete(),
		"users": User.objects.filter(id=id).delete()
	}
	return redirect('/admin', context)

# LOGOUT

def logout(request):
	request.session.clear()
	return redirect('/')


