from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cookie(request):
	print(request.COOKIES)
	resp = HttpResponse('c is for cookie and that is good enough for me...')
	resp.set_cookie('zap', 42)
	resp.set_cookie('sakaicar', 42, max_age = 1000)
	resp.set_cookie('dj4e_cookie','dcc5c249', max_age=1000)
	return resp

def sessfun(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])
    return HttpResponse('view count=' + str(num_visits))