from django.db import models  # не django.contrib

class Client(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    sport = models.CharField(max_length=100, blank=True, null=True)
    trainer = models.CharField(max_length=100, blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)
    month = models.CharField(max_length=20, blank=True, null=True)
    day = models.CharField(max_length=2, blank=True, null=True)
    discount = models.CharField(max_length=50, blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, null=True)
    payment = models.CharField(max_length=50, blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    typeClient = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    channel = models.CharField(max_length=100, blank=True, null=True)  # 👈 добавлено поле

    def __str__(self):
        return f"{self.name} ({self.phone})"
