from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='main_page'),
    path('service_list/', service_list, name='service_list_url'),
    path('panel_items/<str:item_slug>/', service_panel, name='service_panel_url'),
    path('portfolio_panel/', portfolio_panel, name='portfolio_panel'),
    path('contacts/', contacts, name='contacts'),
    path('work/', about_us_panel, name='work'),
    path('production_panel/', production_panel, name='production_panel')
]
