# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "users_project/index.html")

def new(request):
    pass
def create(request):  # Post method sends here..
    pass
def show(request):
    pass
def edit(request):
    pass
def destroy(request):
    pass
