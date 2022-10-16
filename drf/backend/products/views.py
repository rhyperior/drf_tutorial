from ast import Is
from rest_framework import authentication, generics, mixins, permissions

from api.authentication import TokenAuthentication
from api.mixins import StaffEditorPermissionMixin

from .models import Product
from .permissions import IsStaffEditorPermission
from .serializers import ProductSerializer

# Create your views here.


class ProductMixinView(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

        
class ProductListCreateAPIView(StaffEditorPermissionMixin,
                               generics.ListCreateAPIView
                               ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_create(self, serializer):
        # return super().perform_create(serializer)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None or content == '':
            content = "New content bro, what you looking at."
        serializer.save(content=content)

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailedAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
