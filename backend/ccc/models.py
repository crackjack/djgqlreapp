# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class College(models.Model):
	title = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=255, unique=True)
	courses = models.ManyToManyField('Course')

	def __str__(self):
		return self.title

class Course(models.Model):
	title = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=255, unique=True)
	category = models.ForeignKey('Category')

	def __str__(self):
		return self.title

class Category(models.Model):
	title = models.CharField(max_length=50, unique=True)
	slug = models.SlugField(max_length=75, unique=True)

	def __str__(self):
		return self.title
