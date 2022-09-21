from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, 'r') as file:

        file_reader = csv.reader(file, delimiter=",")
        page_name = int(request.GET.get('page', 1))
        content = []

        for row in file_reader:
            content.append({'Name': row[1], 'Street': row[4], 'District': row[6]})
    content.pop(0)
    paginator = Paginator(content, 10)
    bus_stations = paginator.get_page(page_name)


    context = {
         'bus_stations': bus_stations,
    #     'page': ...,
    }
    return render(request, 'stations/index.html', context)
