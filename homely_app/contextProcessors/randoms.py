from django.shortcuts import render, get_list_or_404
from homely_app.models import *
from django.http import Http404,HttpResponse,JsonResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def randoms(request):
    result = {}
    result['randRecipe'] = Recipe.objects.order_by("?").first()
    return result
