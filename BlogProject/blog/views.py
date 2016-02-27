from django.shortcuts import HttpResponse

# Create your views here.

def hello(request):
   name = "Bogo"
   html = "<html><body>Hi %s from views.py. </body></html>" %name
   return HttpResponse(html)
