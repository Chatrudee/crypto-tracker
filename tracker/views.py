from rest_framework import generics
from .models import CryptoPrice
from .serializers import CryptoPriceSerializer

class CryptoPriceList(generics.ListCreateAPIView):
    queryset = CryptoPrice.objects.all()
    serializer_class = CryptoPriceSerializer
