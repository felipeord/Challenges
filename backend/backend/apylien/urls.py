from django.urls import include, path
from rest_framework import routers, views
from . import views
router = routers.DefaultRouter()
router.register(r'AddURLorText', views.TextualcontentViewSet)
router.register(r'Results', views.AnalysisReportSerializer)
router.register(r'issues', views.CustomUserSerializer)
urlpatterns = [
    path('api/', include(router.urls)),

    path('', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('users/', views.UserListView.as_view()),
    path('resultado/', views.AnalisisPorUsuario.as_view()),
    #path('users/', include('users.urls')),
]