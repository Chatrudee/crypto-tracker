from django.contrib import admin
from django.urls import path
from tracker.views import CryptoPriceList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/prices/', CryptoPriceList.as_view()),
]
