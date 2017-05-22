from django.http import HttpResponse
import datetime
def home(request):
    return HttpResponse('<h1 style="color:tomato;text-align:center">This Hello World Is Getting Boring!</h1>')

def current_datetime(request):
    now = datetime.datetime.now
    html = "<html><head></head><body>%s</body></html>" %now
    return HttpResponse(html)
def hours_ahed(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    
    dt=datetime.datetime.now() + datetime.timedelta(hours = offset)
    html="<html><body>In %s hour(s), it will be  %s.</body></html>" %(offset,dt)
    return HttpResponse(html)
