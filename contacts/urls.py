from django.conf.urls import url, include
from rest_framework import routers
from contacts import views

router = routers.DefaultRouter()
router.register(r'contacts', views.ContactViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^readme/', views.readme, name='readme'),
    url(r'^api/', include(router.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/search/?$', views.search, name='search'),
    url(r'^import', views.run_import, name='run_import')
]
