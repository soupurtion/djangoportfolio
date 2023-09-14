from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.
def index(request):


# Render the HTML template index.html with the data in the context variable.
   #return HttpResponse('home page of Sourav')
   return render( request, 'portfolio_app/index.html')