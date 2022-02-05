

from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # routers
    path('', include(('applications.users.urls', 'users'), namespace='users')),
    re_path('', include('applications.product.routes')),
    re_path('', include('applications.sale.routes')),
    
] 