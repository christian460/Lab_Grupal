from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ProductoSerializer

# Create your views here.
def index(request):
    producs=Producto.objects.all()
    return render(request, 'index.html', {'producs':producs})

def agregar(request):
    if request.method == 'POST':
        producto = Producto()
        producto.codigo=request.POST['codigo']
        producto.nombre=request.POST['nombre']
        producto.img=request.FILES.get('img')
        producto.descripcion=request.POST['desc']
        producto.precio=request.POST['precio']
        producto.cantidad=request.POST['cantidad']
        if 'oferta' in request.POST:
            if request.POST['oferta'] == 'on':
                producto.oferta = True
        else:
            producto.oferta = False
        producto.save()
        return redirect('/')
    else:
        return render(request,'agregar.html')

def modificar(request,pro_id):
    prod = get_object_or_404(Producto, pk=pro_id)
    if request.method == 'POST':
        prod.codigo=request.POST['codigo']
        prod.nombre=request.POST['nombre']
        print(prod.img)
        if prod.img != '':
            prod.img=request.FILES.get('img')
        prod.descripcion=request.POST['desc']
        prod.precio=request.POST['precio']
        prod.cantidad=request.POST['cantidad']
        if 'oferta' in request.POST:
            if request.POST['oferta'] == 'on':
                prod.oferta = True
        else:
            prod.oferta = False
        prod.save()
        return redirect('/')
    else:
        return render(request, 'mod.html', {'prod': prod})
    
def lista(request):
    producs=Producto.objects.all()
    return render(request, 'list.html',{'producs':producs} )

def eliminar(request, pro_id):
    prod = get_object_or_404(Producto, pk=pro_id)
    if request.method == 'POST':
        prod.delete()
        return redirect('/')
    else:
        return render(request,'eliminar.html',{'prod':prod})
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
