from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse

from .forms import ContactForm, OrderForm
from .models import *


def main(request):
    context = {}
    context['contact'] = Contacts.objects.last()

    return TemplateResponse(request, "main.html", context)


def project(request):
    context = {}
    context['contact'] = Contacts.objects.last()

    context["inwork"] = RecentlyInWork.objects.all()
    return TemplateResponse(request, "project.html", context)


def contacts(request):
    context = {}
    context['contact'] = Contacts.objects.last()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/complete')

    # if a GET (or any other method) we'll create a blank form
    else:
        context['form'] = ContactForm()

    return TemplateResponse(request, 'contacts.html', context)


def about(request):
    context = {}
    context['contact'] = Contacts.objects.last()
    return TemplateResponse(request, "about.html", context)


def order(request):
    context = {}
    context['contact'] = Contacts.objects.last()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OrderForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/complete')
    else:
        context['form'] = OrderForm()
    return TemplateResponse(request, 'order.html', context)


def service(request):
    context = {}
    context['contact'] = Contacts.objects.last()

    return TemplateResponse(request, "service.html", context)


def complete(request):
    context = {}
    context['contact'] = Contacts.objects.last()
    return TemplateResponse(request, "complete.html", context)

def not_added(request):
    context = {}
    context['contact'] = Contacts.objects.last()
    return TemplateResponse(request, "not_added.html", context)
