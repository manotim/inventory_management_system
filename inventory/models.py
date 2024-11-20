from django.db import models

class Drug(models.Model):
    barcode = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    batch_number = models.CharField(max_length=50)
    expiration_date = models.DateField()
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class StockLog(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=[('in', 'Load'), ('out', 'Offload')])
    quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.drug.name} - {self.action}"
