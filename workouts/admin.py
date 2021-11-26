from django.contrib import admin
from .models import Workouts, Category

class WorkoutsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'sets_reps',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Workouts, WorkoutsAdmin)
admin.site.register(Category, CategoryAdmin)
