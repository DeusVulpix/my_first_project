from django.urls import path
from . import views



app_name = 'products'

urlpatterns = [

    path('', views.products_list_view, name='products-list'),
    path('<int:id>/', views.products_detail_view, name='product-detail'),
    path('create', views.products_create_view, name='product-create'),
    path('<int:id>/update', views.products_upgrade_view, name='product-update'),
    path('<int:id>/delete', views.product_delete_view, name='product-delete')

]
