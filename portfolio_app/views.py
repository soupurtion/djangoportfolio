from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Student, Portfolio, Project
from .forms import ProjectForm, PortfolioForm
# Create your views here.

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["portfolio_project_list"] = Project.objects.filter(portfolio=self.kwargs['pk'])
        return context
    
class ProjectListView(generic.ListView):
    model = Project
class ProjectDetailView(generic.DetailView):
    model = Project


def createProject(request, portfolio_id):
    form = ProjectForm()
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    
    if request.method == 'POST':
        # Create a new dictionary with form data and portfolio_id
        project_data = request.POST.copy()
        project_data['portfolio_id'] = portfolio_id
        
        form = ProjectForm(project_data)
        if form.is_valid():
            # Save the form without committing to the database
            project = form.save(commit=False)
            # Set the portfolio relationship
            project.portfolio = portfolio
            project.save()

            # Redirect back to the portfolio detail page
            return redirect('portfolio-detail', portfolio_id)

    context = {'form': form}
    return render(request, 'portfolio_app/project_form.html', context)


def deleteProject(request,portfolio_id,pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('portfolio-detail', portfolio_id)
    
    return render(request,'portfolio_app/delete_project.html',{'project':project,'portfolio_id':portfolio_id})
    


def updateProject(request,portfolio_id,pk):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    project = Project.objects.filter(pk=pk).values()[0]
    form = ProjectForm(initial=project)

    if request.method == 'POST':
        # Create a new dictionary with form data and portfolio_id
        project_data = request.POST.copy()
        project_data['portfolio_id'] = portfolio_id        
        form = ProjectForm(project_data)

        if form.is_valid():
            # Save the form without committing to the database
            project = form.save(commit=False)
            # Set the portfolio relationship
            project.portfolio = portfolio
            project.id = pk
            project.save()

            # Redirect back to the portfolio detail page
            return redirect('portfolio-detail', portfolio_id)

    context = {'form': form,'portfolio_id':portfolio_id}
    return render(request, 'portfolio_app/update_project.html', context)


def updatePortfolio(request,pk):
    #portfolio = Portfolio.objects.get(pk=pk)
    #print(portfolio)
    portfolio_initial = Portfolio.objects.filter(pk=pk).values()[0]
    form = PortfolioForm(initial=portfolio_initial)
    
    if request.method == 'POST':
        # Create a new dictionary with form data
        portfolio_data = request.POST.copy()
        portfolio_data['id'] =  pk
        form = PortfolioForm(portfolio_data)

        if form.is_valid():
            # Save the form without committing to the database
            portfolio = form.save(commit=False)
            # Set the portfolio relationship
            portfolio.id = pk
            portfolio.save()

            # Redirect back to the portfolio detail page
            return redirect('student-detail', pk)
        
    context = {'form': form,'pk':pk}
    return render(request, 'portfolio_app/update_portfolio.html', context)