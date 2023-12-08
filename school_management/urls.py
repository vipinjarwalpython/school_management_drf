from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenVerifyView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("faculty/", include("faculty.urls")),
    path("faculty/api/", include("faculty.api.urls")),
    path("student/", include("student.urls")),
    path("student/api/", include("student.api.urls")),
    path(
        "api/login/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/login/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"
    ),
    path("api/login/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
