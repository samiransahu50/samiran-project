from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello0(request):
    return HttpResponse("welcome to Inventory Management System")
def index(request):
    return render(request,"inventoryweb/index.html")

