from django.db import models

# Create your models here.

class LoginCredential(models.Model):
    email = models.EmailField( unique=True, null=False, max_length=254)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.email