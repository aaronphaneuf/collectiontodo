from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, CollectionViewSet, UserCollectionViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet, basename='user')
router.register('collection', CollectionViewSet, basename='collection')
router.register('viewcollection', UserCollectionViewSet, basename='viewcollection')

urlpatterns = [ path('', include(router.urls)), ]
