from django.shortcuts import render
from django.http import HttpResponse
import subprocess

# Create your views here.


def activate(request):
    if request.method == 'GET':
        subprocess.run(["ls", "-l"])
        subprocess.call('cd ~', shell=True)
        shell_command = "mapproxy-util autoconfig --capabilities https://geo.egistic.kz/geoserver/global/wms --output /mapproxy/mapproxy.yaml --output-seed /mapproxy/seed.yaml --base /mapproxy/base.yml --force --overwrite /mapproxy/overwrite.yaml"
        subprocess.call(shell_command, shell=True)
        message =  "layer proxied"
    else:
        message = "error with proxy layer"
    return HttpResponse(message)