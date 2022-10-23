from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('select_destination/<str:param>', views.select_destination,
     name="select_destination"),
    path('search_offers/', views.search_offers, name="search_offers"),
    path('price_offers/', views.price_offer, name="price_offer"),
    path('blog/', views.PostList.as_view(), name='home'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail')


   
]