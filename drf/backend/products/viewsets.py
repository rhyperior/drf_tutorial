from rest_framework import mixins, viewsets

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list -> QuerySet
    get -> retrieve -> product Instance detail view
    post -> create new Instance
    put -> update Instance
    patch -> partial Update
    delet -> destroy Instance
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # default
    

class ProductGenericViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    '''
    get -> list -> QuerySet
    get -> retrieve -> product Instance detail view
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # default
