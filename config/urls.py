"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from messaging.urls import router as messaging_router
from payment.urls import router as payment_router
from photo.urls import router as photo_router
from profile.urls import router as profile_router
from swipe.urls import router as swipe_router
from user.urls import router as user_router

# One DefaultRouter combining every app's routes, so /api/ has a single
# browsable root that lists all endpoints.
router = DefaultRouter()
for app_router in (
    user_router,
    profile_router,
    swipe_router,
    photo_router,
    payment_router,
    messaging_router,
):
    router.registry.extend(app_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
