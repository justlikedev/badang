#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import Group
from django.views.static import serve as static_servewe

# admin.autodiscover()
# admin.site.unregister(Group)

urlpatterns = [
    # url(r'^api-auth/', include('rest_framework.urls'))
]
