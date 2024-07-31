from django.urls import path
from .views import UserCreateListView, UserProfileDetailView

urlpatterns = [
    path('testUser/', UserCreateListView.as_view(), name='user-list'),
    path('testUser/<int:user_id>/', UserProfileDetailView.as_view(), name='userprofile-detail'),
]