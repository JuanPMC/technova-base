from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .modeloML import modeloML

from django.core.files.storage import FileSystemStorage

def home(request):
    if request.method == 'POST':
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        prediccion = modeloML(file)
        return HttpResponse("Resultado: {}".format(prediccion.preddiccion))

    return render(request,"home.html")
