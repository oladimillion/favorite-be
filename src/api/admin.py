from django.contrib import admin
from . import models 



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('ranking', 'category_name')

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_date')

class AuditlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created_date')

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Favorite, FavoriteAdmin)
admin.site.register(models.Auditlog, AuditlogAdmin)

