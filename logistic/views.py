from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet


from rest_framework.filters import SearchFilter

from stocks_products.logistic.models import Product, Stock
from stocks_products.logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
    # при необходимости добавьте параметры фильтрации
    filter_backends = [SearchFilter]
    search_fields = ['title','description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    pagination_class = PageNumberPagination
    # при необходимости добавьте параметры фильтрации
    filter_backends = [SearchFilter]
    SearchFilter.search_param = 'products'
    search_fields = ['products__title', 'products__description']