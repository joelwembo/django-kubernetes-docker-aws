from django.urls import path , include
from rest_framework import routers
from .views import CartItemViews , PersonViewSet, SpeciesViewSet


router = routers.DefaultRouter()
router.register(r'people', PersonViewSet)
router.register(r'species', SpeciesViewSet)
# router.register(r'publishers', PublisherListView)

urlpatterns = [
    path('cart-items/', CartItemViews.as_view()),
    path('cart-items/<int:id>', CartItemViews.as_view()),
    # path('publishers/', PublisherListView.as_view()),

]