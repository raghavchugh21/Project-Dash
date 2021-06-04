from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.store, name='store'),
    path('<slug:category_slug>/', views.store, name='products_by_category')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
