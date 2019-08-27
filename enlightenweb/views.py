from django.http import HttpResponse


def index(request):
	return HttpResponse("WENA CABROS VERSION 2.0")