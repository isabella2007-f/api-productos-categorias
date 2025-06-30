from rest_framework import viewsets
from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer
from rest_framework.response import Response
from rest_framework import status

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"mensaje": "Categoría eliminada correctamente"}, status=status.HTTP_200_OK)
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_queryset(self):
        categoria_id = self.request.query_params.get('categoria')
        if categoria_id:
            return Producto.objects.filter(categoria_id=categoria_id)
        return super().get_queryset()
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"mensaje": "Producto eliminado correctamente"}, status=status.HTTP_200_OK)
