from rest_framework.viewsets import ModelViewSet
from  rest_framework.filters import SearchFilter,OrderingFilter,BaseFilterBackend
from  rest_framework.pagination import LimitOffsetPagination
from .models import Product, Stock,StockProduct
from .serializers import ProductSerializer, StockSerializer,ProductPositionSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields=['title','description', ]




class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [SearchFilter]
    search_fields =['positions__product__title']




class StockProductViewSet(ModelViewSet):
    queryset =StockProduct.objects.all()
    serializer_class = ProductPositionSerializer

