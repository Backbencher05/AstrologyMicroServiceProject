from django.urls import path
from .views import AstrologerViewSet, whoami
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'astrologers',AstrologerViewSet, basename='astrologer')

# urlpatterns = [
#     path('astrologers/', AstrologerListCreateView.as_view(), name= 'astrologer-list-create')
# ]

urlpatterns = router.urls + [
    path("whoami/", whoami, name= "whoami"),
]