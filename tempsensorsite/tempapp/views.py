from django.shortcuts import render


def temp(request):
    # The same as commenting out code but just to make it easier
    testing = 0
    # This is the location of your device, the 28-3c01d60784f5 will be diffirent for everyone.
    if testing == 1:
        location = "/sys/bus/w1/devices/28-3c01d60784f5/w1_slave"
        tfile = open(location)
        text = tfile.read()
        tfile.close()
        secondline = text.split("\n")[1]
        temperaturedata = secondline.split(" ")[9]
        temperature = float(temperaturedata[2:])
        celsius = temperature / 1000
        farenheit = (celsius * 1.8) + 32
    else:
        celsius = 23
    context = {"temp": celsius}
    return render(request, "tempapp/main.html", context)