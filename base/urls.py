# base/urls.py

from django.urls import path
from .views import home_view, about_view, project_view, contact_view,ecommerce_detail,juice_detail, portfolio_detail

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('project/', project_view, name='project'),
    path('contact/', contact_view, name='contact'),
    path('ecommerce/', ecommerce_detail, name='ecommerce_detail'),
    path('juice/', juice_detail, name='juice_detail'),
    path('portfolio/', portfolio_detail, name='portfolio_detail'),

]
