from django.shortcuts import render
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.http import *
from django.conf import settings
# import mongoengine
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from datetime import datetime,timedelta
import random,string
# import settings
# import datetime
# from pyUrl.models import * 
# Create your views here.
def checktime(request):
	# time = datatime.datetimenow()
	# print time
	# time = 1
	# allotmentTime = time
	# if time >= allotmentTime:
	# 	return HttpResponse("<h1>The allotment will start on 25th July 2015</h1>")
	# 	# return render_to_response('allot.html')
	# else: 
	# 	return HttpResponse("<h1>The allotment will start on 25th July 2015</h1>")
	# boy = 
	# return HttpResponse("Hello hostellers ")
	return render_to_response("selectCategory.html")

def allotmentform(request):
	if request.POST:
		name = request.POST['name']
		univRoll = request.POST['univRoll']
		year = request.POST['year']
		mobile = request.POST['mobile']
		print name, univRoll, year, mobile
		# name = request.POST['name']
	return render_to_response('allotmentForm.html',context_instance=RequestContext(request))
