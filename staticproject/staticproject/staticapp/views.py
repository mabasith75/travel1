from django.shortcuts import render
from .models import lugar, team


# Create your views here.
def static(request):
    obj = lugar.objects.all()

    return render(request, "index.html", {'result': obj})

def static(request):
    obj2 = team.objects.all()
    return render(request, "index.html", {'result2': obj2})
