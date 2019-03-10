from django.shortcuts import render
from django.http import HttpResponse
import subprocess

# Create your views here.


def activate(request):
    subprocess.run(["ls", "-l"])
    shell_command = "mapproxy-util autoconfig --capabilities https://geo.egistic.kz/geoserver/global/wms --output /mapproxy/mapproxy.yaml --output-seed /mapproxy/seed.yaml --base /mapproxy/base.yaml --force --overwrite /mapproxy/overwrite.yaml"
    subprocess.run(shell_command.split(' '))
    return HttpResponse("heelo world")