from django.urls import path
from . import views
from TaylorsCustomz import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('request/', views.request, name='request'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('gallery/', views.gallery, name='gallery')


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += path('tadmin/', views.AdminListView.as_view(), name='list'),
    urlpatterns += path('tadmin/archived/', views.ArchivedOrders.as_view(), name='archivedList'),
    urlpatterns += path('tadmin/<int:orderNumber>/', views.requestDetail, name='order-detail'),
    urlpatterns += path('tadmin/<int:orderId>/accept', views.accept, name='detail-accept'),
    urlpatterns += path('tadmin/<int:orderId>/deny', views.deny, name='detail-deny'),
    urlpatterns += path('tadmin/<int:orderId>/email', views.email, name='detail-email'),
    urlpatterns += path('tadmin/<int:orderId>/complete', views.complete, name='detail-complete'),
    urlpatterns += path('tadmin/<int:orderId>/delete/', views.delete, name='delete'),
    urlpatterns += path('tadmin/<int:orderId>/archive/', views.archive, name='archive'),


if not settings.DEBUG:
    urlpatterns += path('data/', views.AdminListView.as_view(), name='list'),
    urlpatterns += path('data/archived/', views.ArchivedOrders.as_view(), name='archivedList'),
    urlpatterns += path('data/dashboard', views.admin, name='admin-dash'),
    urlpatterns += path('data/<int:orderNumber>/', views.requestDetail, name='order-detail'),
    urlpatterns += path('data/<int:orderId>/accept', views.accept, name='detail-accept'),
    urlpatterns += path('data/<int:orderId>/deny', views.deny, name='detail-deny'),
    urlpatterns += path('data/<int:orderId>/email', views.email, name='detail-email'),
    urlpatterns += path('data/<int:orderId>/complete', views.complete, name='detail-complete'),
    urlpatterns += path('order/<int:orderId>/delete/',views.delete, name='delete'),
    urlpatterns += path('order/<int:orderId>/archive/', views.archive, name='archive'),


