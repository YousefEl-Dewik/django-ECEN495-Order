from django.db import models

# Create your models here.
class Order(models.Model):
    orderName = models.CharField(max_length=100)  # column
    price = models.DecimalField(max_digits=19, decimal_places=2) # 250.99
    quantity = models.DecimalField(max_digits=100000, decimal_places=0)
    photo = models.ImageField(upload_to='Order')  # max_length=50
    barcode_id = models.IntegerField(default=0)
    
    # category = models.ForeignKey()

    def str(self):
        return self.orderName