from django import db
from django.shortcuts import render, redirect, get_list_or_404
from rest_framework import generics, permissions
from rest_framework.views import APIView

from django.http import Http404,HttpResponse,JsonResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django import template
from django.shortcuts import get_object_or_404, get_list_or_404
from homely_app.models import *
from django.db import connections, transaction
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from django.utils import timezone
from django.views.generic.detail import DetailView


def index(request):
    return render(request, 'index.html')

def recetas(request):
    return render(request, 'recetas.html', {'recetas': Recipe.objects.all(), 'tags': Tag.objects.all()})

def receta(request, pk):
    return render(request, 'recetas.html', {'receta': Recipe.objects.get(pk=pk), 'tags': Tag.objects.all()})