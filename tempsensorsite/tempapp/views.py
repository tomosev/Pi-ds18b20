from django.shortcuts import render


def temp(request):
    # This is the location of your device, the 28-3c01d60784f5 will be diffirent for everyone.
    location = "/sys/bus/w1/devices/28-3c01d60784f5/w1_slave"
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature / 1000
    farenheit = (celsius * 1.8) + 32
    context = {"temp": celsius}
    return render(request, "tempapp/main.html", context)