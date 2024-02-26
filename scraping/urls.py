from django.urls import path
from .views import home_view, list_view
from scraping.views import handler400, handler403, handler404, handler500


app_name = 'scraping'

urlpatterns = [
    path('', home_view, name='home'),
    path('list/', list_view, name='list'),

    path('400/', handler400, name='handler400'),
    path('403/', handler403, name='handler403'),
    path('404/', handler404, name='handler404'),
    path('500/', handler500, name='handler500'),
]

