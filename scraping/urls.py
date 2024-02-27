from django.urls import path
from .views import home_view, VDetail, VList, VCreate, VUpdate, VDelete
from scraping.views import handler400, handler403, handler404, handler500


app_name = 'scraping'

urlpatterns = [
    path('', home_view, name='home'),
    path('list/', VList.as_view(), name='list'),
    path('detail/<int:pk>/', VDetail.as_view(), name='v_detail'),
    path('create/', VCreate.as_view(), name='create'),
    path('update/<int:pk>', VUpdate.as_view(), name='update'),
    path('delete/<int:pk>', VDelete.as_view(), name='delete'),

    path('400/', handler400, name='handler400'),
    path('403/', handler403, name='handler403'),
    path('404/', handler404, name='handler404'),
    path('500/', handler500, name='handler500'),
]

