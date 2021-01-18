from django.urls import path
from . import views
from TaylorsCustomz import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('request/', views.request, name='request'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.bio, name='bio'),
    path('data/', views.AdminListView.as_view(), name='list'),
    path('data/archived/', views.ArchivedOrders.as_view(), name='archivedList'),
    path('data/dashboard', views.admin, name='admin-dash'),
    path('data/<int:orderNumber>/', views.requestDetail, name='order-detail'),
    path('data/<int:orderId>/accept', views.accept, name='detail-accept'),
    path('data/<int:orderId>/deny', views.deny, name='detail-deny'),
    path('data/<int:orderId>/email', views.email, name='detail-email'),
    path('data/<int:orderId>/complete', views.complete, name='detail-complete'),
    path('order/<int:orderId>/delete/',views.delete, name='delete'),
    path('order/<int:orderId>/archive/', views.archive, name='archive'),
    path('data/dashboard/', views.admin, name='admin'),
    path('data/ratings/<int:id>', views.rating, name='rating-review')


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



    


