from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    station = []
    with open(settings.BUS_STATION_CSV, encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            station.append({
            'Name': row['Name'],
            'Street': row['Street'],
            'District': row['District'],
            })
    paginator = Paginator(station, 10)
    pagination_number = request.GET.get('page', 1)
    page = paginator.get_page(pagination_number)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
