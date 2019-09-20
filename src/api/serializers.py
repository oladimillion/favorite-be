import json
from rest_framework import serializers
from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

    def create(self, validated_data):
        """
        create a new category or update the rank of an existing category
        """
        ModelClass = self.Meta.model
        category_name = validated_data.get('category_name')
        ranking = validated_data.get('ranking')
        instance = None
        try:
            instance = ModelClass.objects.get(category_name__iexact=category_name)
            instance.ranking = ranking
            instance.save()
        except:
            instance = ModelClass.objects.create(**validated_data)
        return instance


class FavoriteSerializer(serializers.ModelSerializer):
    category_detail = serializers.SerializerMethodField()

    class Meta:
        model = models.Favorite 
        fields = '__all__'

    def get_category_detail(self, obj):
        return CategorySerializer(obj.category).data

    def validate_description(self, value):
        """
        Validates the description length
        """
        if value and (len(value) < 10):
            raise serializers.ValidationError(
                    'This field must be at least 10 characters'
                )
        return value


class AuditlogSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()
    class Meta:
        model = models.Auditlog 
        fields = '__all__'

    def get_content(self, obj):
        return json.loads(obj.content)
