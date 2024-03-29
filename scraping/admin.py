from django.contrib import admin
from .models import City, Language, Vacancy, Error, Url


admin.site.register(City)
admin.site.register(Language)
admin.site.register(Error)
admin.site.register(Url)


class VacancyAdmin(admin.ModelAdmin):
    search_fields = ['url', 'title', 'company', 'description']


admin.site.register(Vacancy, VacancyAdmin)

