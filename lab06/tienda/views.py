from .models import Producto, Categoria 
from django.shortcuts import get_object_or_404,render

# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categorias = Categoria.objects.all()
    context = {'product_list': product_list, 'categorias': categorias}
    return render(request,'index.html',context)


def producto (request):
    
    return render(request,'producto.html')
def lista_productos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    context = {'categoria': categoria, 'productos': productos}
    return render(request, 'lista_productos_por_categoria.html', context)