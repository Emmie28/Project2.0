from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_listing, name="create"),
    path("active_listing", views.active_listing, name="active_listing"),
    path("listing/<str:name>", views.listing, name="listing"),
    path("add_watch_list/<str:item>", views.add_watch_list, name="add_watch_list"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("categories", views.categories, name="categories"),
    path("category_list/<str:category>", views.category_list, name="category_list"),
    path("close_bid/<str:name>", views.close_bid, name="close_bid")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
