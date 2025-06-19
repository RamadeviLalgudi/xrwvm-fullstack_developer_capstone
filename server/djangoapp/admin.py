from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 2

# CarModelAdmin class
class CarMakeAdmin(admin.ModelAdmin):


    inlines = [CarModelInline]
    list_display = ['name', 'description']

# CarMakeAdmin class with CarModelInline
class CarModelAdmin(admin.ModelAdmin):


    list_display = ['car_make', 'name', 'type', 'year', 'color']
    list_filter = ['car_make']
    search_fields = ['car_make', 'name', 'type']

# Register models here
admin.site.register(CarMake)


admin.site.register(CarModel)
