from django.db import models

class User(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	email = models.CharField(max_length = 50)
	password = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


class Model(models.Model):
	title = models.CharField(max_length = 50)
	category = models.CharField(max_length = 50)
	description = models.CharField(max_length = 255)
	format = models.CharField(max_length = 50)
	rating = models.CharField(max_length = 10)
	tag = models.TextField()
	cover = models.TextField()
	link = models.TextField()
	author = models.ForeignKey(User, related_name = "models")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


class Comment(models.Model):
	content = models.CharField(max_length = 255)
	sender = models.ForeignKey(User, related_name = "comments")
	receiver = models.ForeignKey(Model, related_name = "comments")
	created_at = models.DateTimeField(auto_now_add = True)
