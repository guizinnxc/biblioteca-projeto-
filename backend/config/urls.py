from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('leitores.urls')),
    path('api/', include('livros.urls')),
    path('api/', include('emprestimos.urls')),
]
