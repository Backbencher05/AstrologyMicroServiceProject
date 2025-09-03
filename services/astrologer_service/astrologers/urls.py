from django.urls import path
from .views import AstrologerListCreateView 


urlpatterns = [
    path('astrologers/', AstrologerListCreateView.as_view(), name= 'astrologer-list-create')
]