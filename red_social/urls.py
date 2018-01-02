"""red_social URL Configuration


"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from apps.api import views
from rest_framework_mongoengine import routers
from rest_framework_jwt.views import obtain_jwt_token

# this is DRF router for REST API viewsets
router = routers.DefaultRouter()

# register REST API endpoints with DRF router
router.register(r'publicacion', views.PublicacionViewSet, r"publicacion")
router.register(r'user', views.UserViewSet, r"user")
router.register(r'perfil', views.PerfilViewSet,r"perfil")
router.register(r'categoriapost', views.CategoriaPostViewSet,r"categoriapost")
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
]
