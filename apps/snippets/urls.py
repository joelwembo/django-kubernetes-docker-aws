from django.urls import path
from apps.snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

#from apps.snippets.views import SalesListAPIView

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),

    path('sales/', views.sales_list),

]

urlpatterns = format_suffix_patterns(urlpatterns)
