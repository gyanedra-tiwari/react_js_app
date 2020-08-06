from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers
from .views import ProfileViewSet, TagsViewSet, UserViewSet
from . import views

snippet_highlight = ProfileViewSet.as_view({
    'get': 'highlight'
})
snippet_add_hosts = ProfileViewSet.as_view({
    'get': 'addhost'
})
snippet_update_device_token = UserViewSet.as_view({
    'post': 'update_device_token'
})
print("I am here")
router = routers.SimpleRouter(trailing_slash=False)
# router.register(r'profile', UserProfileViewSet, base_name='profile')
router.register(r'user_list', UserViewSet, basename='user_list')


urlpatterns = router.urls
urlpatterns = urlpatterns + [
    url(r'register', views.create_user_profile),
    url(r'forgot-password', views.forgot_password),
    url(r'reset-password', views.reset_password),
    url(r'update-device-token', snippet_update_device_token),

    # url(r'^get_user$', snippet_highlight, name='get_user'),
    url(r'^get_doctors$', snippet_add_hosts, name='get_doctors'),

]


