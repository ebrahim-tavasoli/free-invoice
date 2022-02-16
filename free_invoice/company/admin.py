from django.contrib import admin

from company import models


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    pass
