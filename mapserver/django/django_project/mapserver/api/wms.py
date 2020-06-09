__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '09/06/20'

import requests
from urllib.parse import unquote
from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden


def wms(request):
    if request.method == 'GET':
        params = unquote(request.build_absolute_uri().split('?')[1].lower())
        params = params.replace('kartoza:', '')
        mapserver_url = '{}?{}'.format(settings.MAPSERVER_PUBLIC_WMS_URL, params)
        response = requests.get(mapserver_url)
        return HttpResponse(
            content=response.content,
            status=response.status_code,
            content_type=response.headers['Content-Type']
        )
    else:
        return HttpResponseForbidden(
            'Method is forbidden')
