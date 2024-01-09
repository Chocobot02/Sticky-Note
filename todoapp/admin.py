from django.contrib import admin
from todoapp.models import todolist
# Register your models here.

# admin.site.register(todolist)

class todoadmin(admin.ModelAdmin):
    # fields = ['priority', 'todo'] #arrangement only
    # use for organizing base on type
    fieldsets = [('ToDos', {'fields':['todo', 'priority']}),
                  ('Created Dates', {'fields':['created']})] 
    

admin.site.register(todolist, todoadmin)
