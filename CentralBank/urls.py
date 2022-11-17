from django.contrib import admin
from django.urls import include, re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$', views.index, name = "home"),
    re_path(r'^accounts/', include("accounts.urls")),
    re_path(r'^profile/', include("profiles.urls")),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Trybe Bank"
admin.site.site_title = "Trybe Bank Administration"
admin.site.index_title = "Bem-vindo à página de Administrador do Trybe Bank"
