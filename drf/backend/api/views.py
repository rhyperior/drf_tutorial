import json
# from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API view
    """
    # instance = Product.objects.all().order_by("?").first()
    # print(request)
    # data = request.data
    # if instance:
    #     # data = model_to_dict(instance, fields=['id', 'content', 'price'])
    #     data = ProductSerializer(instance).data
    # print(data)
    # return JsonResponse(data, headers={"Content-Type": "application/json"})
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # data = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid request": "Fields not valid"}, status=400)