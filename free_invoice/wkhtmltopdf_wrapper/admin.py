from django.contrib import admin

from wkhtmltopdf_wrapper import models


@admin.register(models.WkhtmltopdfLog)
class WkhtmltopdfLogAdmin(admin.ModelAdmin):
    pass
