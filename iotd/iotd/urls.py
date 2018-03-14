from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import serializers, status
from rest_framework import views as rest_views
from rest_framework.response import Response
from django.conf import settings

from django.views import generic
from index import views
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls.static import static

class MessageSerializer(serializers.Serializer):
    message = serializers.CharField()

class EchoView(rest_views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED)

schema_view = get_swagger_view(title='limdongjin API', url='/docs')

router = routers.DefaultRouter()
# refill your ViewSet

'''
ex)

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'bills', views.BillViewSet)
router.register(r'people', views.PeopleViewSet)
router.register(r'analyses', views.AnalysesViewSet)
router.register(r'footchairs', views.FootchairsViewSet)
router.register(r'newkeywords', views.NewkeywordsViewSet)
'''

def staticfiles_urlpatterns(prefix=None):
    """
        Helper function to return a URL pattern for serving static files.
    """
    if prefix is None:
        prefix = settings.STATIC_URL
    return static(prefix, view='django.contrib.staticfiles.views.serve')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', generic.RedirectView.as_view(
         url='/docs/', permanent=False)),
    url(r'^', include(router.urls)),
    url(r'^docs/', schema_view, name="schema_view"),
    url(r'^api/auth/', include(
        'rest_framework.urls', namespace='rest_framework')),
    url(r'^api/auth/token/obtain/$', TokenObtainPairView.as_view()),
    url(r'^api/auth/token/refresh/$', TokenRefreshView.as_view()),
    url(r'^api/echo/$', EchoView.as_view()),

    url(r'^api/testbill/$', views.BillViewSet.as_view({'get': 'TestBill'}))
]

if settings.DEBUG and not urlpatterns:
    urlpatterns += staticfiles_urlpatterns()

