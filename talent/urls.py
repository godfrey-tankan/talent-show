
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('talentsystem.urls')),
    # path('api/', include('authy.api_urls')),

]
