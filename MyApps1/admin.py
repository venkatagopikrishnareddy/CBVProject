from django.contrib import admin
from MyApps1.models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ["title","author","pages","price"];

admin.site.register(Book, BookAdmin)


#DetailView
from django.contrib import admin
from MyApps1.models import Company
#Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display=['name', 'location','ceo'];
admin.site.register(Company,CompanyAdmin)



from MyApps1.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','name','salary','company'];
admin.site.register(Employee,EmployeeAdmin)


