from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view 
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from .filters import ProductFilter
from .models import Product
from .serializers import ProductSerializer
# Create your views here.

@api_view(['GET'])
def get_products(request):
    filterset = ProductFilter(request.GET,queryset=Product.objects.all().order_by('id'))
    respage = 4 
    paginator = PageNumberPagination()
    paginator.page_size = respage
    queryset = paginator.paginate_queryset(filterset.qs, request)
    serializer = ProductSerializer(queryset,many=True)
    return Response({"products":serializer.data})


@api_view(['GET'])
def get_id_product(request,pk):
    products = get_object_or_404(Product,id=pk)
    serializer = ProductSerializer(products,many=False)
    print(products)
    return Response({"products":serializer.data})



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_product(request):
    data = request.data
    serializer = ProductSerializer(data=data)

    if serializer.is_valid():
        product = Product.objects.create(**data,user=request.user)
        res = ProductSerializer(product, many=False)
    
        return Response({"products":res.data})
    else:
        return Response(serializer.errors)


