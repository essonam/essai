from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    context = {"message":"bonjour a tous"}
    template = loader.get_template("app/index.html")
    print("je suis tres fort et tres pop")
    return HttpResponse(template.render(context,request))
