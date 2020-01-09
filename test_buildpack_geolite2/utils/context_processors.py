from django.conf import settings
from django.contrib.gis.geoip2 import GeoIP2

geoip = GeoIP2()

def geoip_context(request):
    return {"geoip_city": geoip.city(client_ip(request))}

def client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def settings_context(_request):
    return {"settings": settings}
