from django.contrib import admin
from core import models
from django.contrib.auth.admin import UserAdmin
from .models import User

class CompanyeAdmin(admin.ModelAdmin):
    list_display = ('pk','name')

class BranchAdmin(admin.ModelAdmin):
    list_display = ('pk','name')

class StaffAdmin(admin.ModelAdmin):
    list_display = ('branch','name')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ( "pk",'name','surname',"staff", "staff_type")

class MessageAdmin(admin.ModelAdmin):
    list_display = ("pk",'from_user','to_id','is_deleted','is_send','is_read','time')

class EmployeeEducationAdmin(admin.ModelAdmin):
    list_display = ( "pk",'employee_id',"education_type", "education_center","edu_from_date","edu_to_date",)

class EmployeeLanguageAdmin(admin.ModelAdmin):
    list_display = ('emplooyee','language','language_level','certificate_number','certificate_date')

class EmployeeExperienceAdmin(admin.ModelAdmin):
    list_display = ('employee','work_place','exp_from_date','exp_to_date','position')

admin.site.register(User, UserAdmin)

admin.site.register(models.Companye,CompanyeAdmin)
admin.site.register(models.Branch,BranchAdmin)
admin.site.register(models.Staff,StaffAdmin)
admin.site.register(models.StaffType)
admin.site.register(models.Gender)
admin.site.register(models.Employee,EmployeeAdmin)
admin.site.register(models.EducationType)
admin.site.register(models.EmployeeEducation,EmployeeEducationAdmin)
admin.site.register(models.EmployeeExperience,EmployeeExperienceAdmin)
admin.site.register(models.Language)
admin.site.register(models.LanguageLevel)
admin.site.register(models.EmployeeLanguage,EmployeeLanguageAdmin)
admin.site.register(models.Message,MessageAdmin)