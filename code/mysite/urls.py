import debug_toolbar
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # include the URLs of the 'blog' package
    path('', include('blog.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
