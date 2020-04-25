from django.contrib import admin
from core.models import Clinic, Department, Doctor, Consultant


@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rating', 'status')
    ordering = ('-rating',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'clinic', 'direction', 'floor')


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'clinic', 'department', 'avatar', 'experience')
    ordering = ('-experience',)


@admin.register(Consultant)
class Consultant(admin.ModelAdmin):
    list_display = ('id', 'clinic', 'department', 'avatar', 'phone')
