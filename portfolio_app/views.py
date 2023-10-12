from django.shortcuts import render
from django.views import generic
from .models import Student, Portfolio, Project

# Create your views here.
from django.http import HttpResponse
# Create your views here.


def index(request):
# Render the HTML template index.html with the data in the context variable.
   #return HttpResponse('home page of Sourav')
    #return render( request, 'portfolio_app/index.html')
    student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
    print("active portfolio query set", student_active_portfolios)
    return render( request, 'portfolio_app/index.html', {'student_active_portfolios':student_active_portfolios})


class StudentListView(generic.ListView):
    model = Student
class StudentDetailView(generic.DetailView):
    model = Student

class PortfolioDetailView(generic.DetailView):
    model = Portfolio

class ProjectListView(generic.ListView):
    model = Project
class ProjectDetailView(generic.DetailView):
    model = Project