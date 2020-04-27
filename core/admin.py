from django.contrib import admin
from core.models import Clinic, Department, Doctor, Consultant, Service, TherapyDocument, Order


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
class ConsultantAdmin(admin.ModelAdmin):
    list_display = ('id', 'clinic', 'department', 'avatar', 'phone')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'clinic', 'title', 'price', 'cabinet')


@admin.register(TherapyDocument)
class TherapyDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'therapy', 'doctor')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'doctor', 'client', 'created_at')
