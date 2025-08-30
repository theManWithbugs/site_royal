from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from setup import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('admin_royal/', include('admin_royal.urls'))
]
