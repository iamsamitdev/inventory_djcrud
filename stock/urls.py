from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('create_product', views.create_product, name='create_product'),
    path('product/<int:product_id>/update', views.update_product, name='update_product'),
    path('product/<int:product_id>/delete', views.delete_product, name='delete_product'),
]
