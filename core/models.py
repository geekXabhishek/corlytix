from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class LoginCredential(models.Model):
    email = models.EmailField(unique=True, null=False, max_length=254)
    password = models.CharField(max_length=255)  # store hashed password
    role = models.CharField(
        max_length=20,
        choices=[("client", "Client"), ("manager", "Manager")],
        default="client"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} ({self.role})"

    # Hash password before saving
    def save(self, *args, **kwargs):
        if not self.id:  # only hash on creation
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    # Password check method
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
