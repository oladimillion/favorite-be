from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Auditlog(BaseModel):
    favorite = models.ForeignKey('api.Favorite', on_delete=models.CASCADE)
    content = models.TextField()

    class Meta:
        ordering = ['-created_date']


class Category(BaseModel):
    ranking = models.IntegerField(null=True)
    category_name = models.CharField(max_length=50)

    class Meta:
        ordering = ['ranking']

    def save(self, *args, **kwargs):
        self.category_name = self.category_name.lower()
        return super(Category, self).save(*args, **kwargs)


class Favorite(BaseModel):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_date']


