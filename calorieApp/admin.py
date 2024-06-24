from django.contrib import admin
from calorieApp.models import Custom_user, calorieInfo, foods



# Register your models here.
admin.site.register(Custom_user)
admin.site.register(calorieInfo)
admin.site.register(foods)
