from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    PRIORITY = [
        ("H", "High"),
        ("M", "Medium"),
        ("L", "Low"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) #(auto_now) >> تسجيل تاريخ التعديل و الإنشاء

    def __str__(self):
        return self.title