#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url, include

urlpatterns = [
    url(r'^api-token-auth/', include('rest_framework.urls'))
]
