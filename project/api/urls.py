from django.conf.urls import url, include
from rest_framework import routers
from project.api.views import (
    UserViewSet, GroupViewSet, SquadViewSet, SoldierViewSet
    )

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'squads', SquadViewSet)
router.register(r'soldiers', SoldierViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
