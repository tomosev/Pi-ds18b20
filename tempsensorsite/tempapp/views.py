from django.shortcuts import render
from tempapp import tempsensor

temp = tempsensor.loop(ds18b20)


def temp(request):
    context = {"temp": temp}
    return render(request, "tempapp/main.html", context)