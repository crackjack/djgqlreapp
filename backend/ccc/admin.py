# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import College, Course, Category

class CollegeAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',), }

admin.site.register(College, CollegeAdmin)


class CourseAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',), }

admin.site.register(Course, CourseAdmin)


class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',), }

admin.site.register(Category, CategoryAdmin)
