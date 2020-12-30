from django.urls import path
from . import views
from TaylorsCustomz import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('request/', views.request, name='request'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('display/', views.displayDetail, name='display-detail'),
    path('gallery/', views.gallery, name='gallery')


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns +=  path('tadmin/', views.AdminListView.as_view(), name='list'),
    urlpatterns += path('tadmin/<int:orderId>/', views.requestDetail, name='list-detail'),
    urlpatterns += path('tadmin/<int:orderId>/accept', views.accept, name='detail-accept'),
    urlpatterns += path('tadmin/<int:orderId>/deny', views.deny, name='detail-deny'),
    urlpatterns += path('tadmin/<int:orderId>/email', views.email, name='detail-email'),
    urlpatterns += path('tadmin/<int:orderId>/delete/', views.delete, name='delete'),


if not settings.DEBUG:
    urlpatterns += path('admin/', views.AdminListView.as_view(), name='list'),
    urlpatterns += path('admin/dashboard', views.admin, name='admin-dash'),
    urlpatterns += path('admin/<int:orderId>/', views.requestDetail, name='list-detail'),
    urlpatterns += path('admin/<int:orderId>/accept', views.accept, name='detail-accept'),
    urlpatterns += path('admin/<int:orderId>/deny', views.deny, name='detail-deny'),
    urlpatterns += path('admin/<int:orderId>/email', views.email, name='detail-email'),
    urlpatterns += path('admin/<int:orderId>/delete/',views.delete, name='delete'),



