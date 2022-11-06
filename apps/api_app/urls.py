from django.urls import path , include
from rest_framework import routers
from .views import CartItemViews , PersonViewSet, SpeciesViewSet, MenuViewSet


router = routers.SimpleRouter()
router.register(r'people', PersonViewSet)
router.register(r'species', SpeciesViewSet)

urlpatterns = [
    path('cart-items/', CartItemViews.as_view()),
    path('cart-items/<int:id>', CartItemViews.as_view()),
    path('menu/', MenuViewSet.as_view({'get': 'list'})),

]