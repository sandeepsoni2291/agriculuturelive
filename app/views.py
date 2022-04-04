from django.shortcuts import render
from app.models import *

# Create your views here.
def index(request):
    querySet = Product.objects.all()
    return render(request, 'app/index.html', {'data': querySet})