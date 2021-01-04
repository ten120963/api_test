from django.shortcuts import render
from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer

class CourseView(viewsets.ModelViewSet):
	#added comment
	queryset = Course.objects.all()
	serializer_class = CourseSerializer
