from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True,null=True)
	banner = models.ImageField(upload_to='images/banner_categories',blank=True,null=True)
	sort_order = models.IntegerField(default=0)
	status = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to='images/data',blank=True,null=True)
	description = models.TextField()
	sku = models.CharField(max_length=100,unique=True)
	price = models.DecimalField(max_digits=11, decimal_places=2)
	category = models.ForeignKey(Category)
	status = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name
