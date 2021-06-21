"""library URL Configuration

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
from django.urls import path, re_path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

import knihovna

handler404 = 'knihovna.views.error_404'
handler403 = 'knihovna.views.error_403'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('knihovna/', include('knihovna.urls')),
    path('', RedirectView.as_view(url='knihovna/')),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^403/$', knihovna.views.error_403),
    re_path(r'^404/$', knihovna.views.error_404),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                             document_root=settings.MEDIA_ROOT)

