#from django.shortcuts import render
#from.models import Producto, Categoria
#from django.shortcuts import get_object_or_404, render
# Create your views here.


#from django.db.models import Count

#def index(request):
#    product_list = Producto.objects.order_by('nombre')[:7]
#    category_list = Producto.objects.values('categoria__nombre').annotate(total=Count('categoria__nombre'))
#    context = {'product_list': product_list, 'category_list': category_list}
#    return render(request,'index.html', context)

#def producto (request,producto_id ):
#    producto = get_object_or_404(Producto, pk=producto_id)
#    #print(producto.imagen.url) 
#    return render(request,'producto.html', {'producto': producto})
    
#def category(request, category_name):
#    category = get_object_or_404(Categoria, nombre=category_name)
#    product_list = category.producto_set.all()
#    category_list = Producto.objects.values('categoria__nombre').annotate(total=Count('categoria__nombre'))
#    context = {'product_list': product_list, 'category_list': category_list}
#    return render(request, 'category.html', context)



from rest_framework import generics
from .models import Producto, Categoria
from .serializer import ProductoSerializer, CategoriaSerializer

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer