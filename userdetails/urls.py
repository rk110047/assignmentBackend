from django.urls import path
from .views import UserDetailsListAPIView,UserDetailsCreateAPIView


urlpatterns=[
    path('list/',UserDetailsListAPIView.as_view(),name="user-detaisl-list"),
    path('create/',UserDetailsCreateAPIView.as_view(),name="user-details-create")
    # path('create/')
]