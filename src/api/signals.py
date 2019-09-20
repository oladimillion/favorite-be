import json
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import models, serializers


@receiver(post_save, sender=models.Favorite)
def post_favorite_save(sender, instance, **kwargs):
    serializer = serializers.FavoriteSerializer(instance)
    json_data = json.dumps(serializer.data)
    models.Auditlog.objects.create(favorite=instance, content=json_data)
