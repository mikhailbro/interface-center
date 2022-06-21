"""interfacecenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from app_interface import views as interface_views
from app_implementation import views as implementation_views
from app_application import views as application_views
from app_review import views as review_views
from app_user import views as user_views

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'interfaces', interface_views.InterfaceViewSet)
router.register(r'users', interface_views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', interface_views.index, name='index'),
    path('interfaces/', include('app_interface.urls')),

    path('implementations/', include('app_implementation.urls')),
    path('applications/', include('app_application.urls')),
    path('reviews/', include('app_review.urls')),

    path('account/', include('app_user.urls')),

    path('interface_actions/', include('app_interface_actions.urls')),
    path('implementation_actions/', include('app_implementation_actions.urls')),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

# admin.site.site_header = 'ACME Interface Center Administration'
# admin.site.site_title  =  "ACME IC admin site"
# admin.site.index_title  =  "ACME IC Admin"
