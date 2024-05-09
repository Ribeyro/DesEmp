#from django.urls import path
#from . import views

#app_name = 'tienda'
#urlpatterns = [
#    path('', views.index, name='index'),
#    path('producto/<int:producto_id>/', views.producto, name='producto'),
#    path('category/<str:category_name>/', views.category, name='category')
#    
#    ]
from django.urls import path
from .views import CategoriaList, CategoriaDetail, ProductoList, ProductoDetail

urlpatterns = [
    path('categorias/', CategoriaList.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', CategoriaDetail.as_view(), name='categoria-detail'),
    path('productos/', ProductoList.as_view(), name='producto-list'),
    path('productos/<int:pk>/', ProductoDetail.as_view(), name='producto-detail'),
]