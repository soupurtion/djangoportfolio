from django.contrib import admin
from .models import Student, Portfolio, Project#,ProjectsInPortfolio
# Register your models here.


# Register your models here so they can be edited in admin panel
admin.site.register(Student)
admin.site.register(Portfolio)
admin.site.register(Project)
#admin.site.register(ProjectsInPortfolio)