
from django.urls import path
from SampleDBProject import views
from django.conf.urls.static import static
from django.conf.urls import include
from . import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('admin/', include("admin.login.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
