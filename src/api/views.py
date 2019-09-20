from rest_framework import (
            viewsets, 
            generics,
            response, 
            permissions,
            status,
        )

from django_filters.rest_framework import DjangoFilterBackend

from . import models, serializers, pagination

class FavoriteViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Favorite instances.
    """
    serializer_class = serializers.FavoriteSerializer 
    queryset = models.Favorite.objects.all()
    http_method_names = ['get', 'post', 'put', 'options']
    pagination_class = pagination.ContentPagination

    def create(self, request, *args, **kwargs):
        category_serializer = self.create_or_update_category(request)
        request.data['category'] = category_serializer.data.get('id')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()

        if request.data.get('category_name'):
            category_serializer = self.create_or_update_category(request)
            request.data['category'] = category_serializer.data.get('id')

        serializer = self.get_serializer(
                instance, 
                data=request.data, 
                partial=partial
            )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return response.Response(serializer.data)

    def create_or_update_category(self, request):
        serializer = serializers.CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer


class CategoryListAPIView(generics.ListAPIView):
    """
    Get category list 
    """
    serializer_class = serializers.CategorySerializer 
    queryset = models.Category.objects.all()


class AuditlogListAPIView(generics.ListAPIView):
    """
    Get auditlog by favorite id passed into request params 
    """
    serializer_class = serializers.AuditlogSerializer 
    queryset = models.Auditlog.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['favorite']

