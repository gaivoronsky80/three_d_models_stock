from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')

class userManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 3 or not postData['first_name'].isalpha():
            errors['first_name'] = 'Please enter a first name'
        if len(postData['last_name']) < 3 or not postData['last_name'].isalpha():
            errors['last_name'] = 'Please enter a last name'
        if len(postData['email']) < 1:
            errors['email'] = "Please enter an email"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors['password'] ='Password must contain 8 characters'
        elif not PASSWORD_REGEX.match(postData['password']):
            errors['password'] = 'Password must contain at least one uppercase and one number'
        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = "Passwords do not match"
        print(errors)
        return errors

class User(models.Model):
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	password = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = userManager()


class Model(models.Model):
	title = models.CharField(max_length = 50)
	category = models.CharField(max_length = 50)
	description = models.CharField(max_length = 255)
	format = models.CharField(max_length = 50)
	rating = models.CharField(max_length = 10)
	tag = models.TextField()
	cover = models.ImageField(upload_to = 'media')
	link = models.FileField(upload_to = 'media')
	author = models.ForeignKey(User, related_name = "models")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = userManager()


class Comment(models.Model):
	content = models.CharField(max_length = 255)
	sender = models.ForeignKey(User, related_name = "comments")
	receiver = models.ForeignKey(Model, related_name = "comments")
	created_at = models.DateTimeField(auto_now_add = True)
	
	objects = userManager()
