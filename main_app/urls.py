from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('brands/', views.brands_index, name='index'),
    path('brands/<int:brand_id>/', views.brands_detail, name='detail'),
    path('brands/create/', views.BrandCreate.as_view(), name='brands_create'),
    path('brands/<int:pk>/update/',
         views.BrandUpdate.as_view(),
         name='brands_update'),
    path('brands/<int:pk>/delete/',
         views.BrandDelete.as_view(),
         name='brands_delete'),
    path('brands/<int:brand_id>/add_purchase',
         views.add_purchase,
         name='add_purchase'),
    path('brands/<int:brand_id>/assoc_product/<int:product_id>/',
         views.assoc_product,
         name='assoc_product'),
    path('accounts/signup/', views.signup, name='signup'),
]
