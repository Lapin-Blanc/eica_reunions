from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Reunion

# Create your views here.
@login_required(login_url='/admin/login/')
def home(request, id):
    r = Reunion.objects.get(pk=id)
    return render(request, "pv_reunion.html", context={
            "reunion": r,
            }
    )
