from django.shortcuts import render_to_response
from django.http import HttpResponse

import models


def myfirstview(request):
	return HttpResponse("Hello Guys!! This is the Home Page of News App")

