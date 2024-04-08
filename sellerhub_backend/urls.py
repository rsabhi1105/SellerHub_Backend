from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/api/", include("authentications.urls")),
    path("user/api/", include("customer_panel.urls")),
    path("user/api/", include("seller_panel.urls")),
    path("user/api/", include("testing_app.urls")),
    path("user/api/", include("payment_api.urls")),
    path("user/api/", include("contact.urls")),
    path("user/api/", include("chat_bot.urls")),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
