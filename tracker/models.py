from django.db import models

class CryptoPrice(models.Model):
    name = models.CharField(max_length=50) # ชื่อเหรียญ เช่น Bitcoin
    price = models.DecimalField(max_digits=20, decimal_places=2) # ราคา
    timestamp = models.DateTimeField(auto_now_add=True) # เวลาที่บันทึก

    def __str__(self):
        return f"{self.name} - {self.price}"
