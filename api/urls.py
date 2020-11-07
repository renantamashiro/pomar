from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    path('api/specie/', views.SpecieList.as_view()),
    path('api/specie/<int:pk>/', views.SpecieDetail.as_view()),
    path('api/tree/', views.TreeList.as_view()),
    path('api/tree/<int:pk>/', views.TreeDetail.as_view()),
    path('api/tree-group/', views.TreeGroupList.as_view()),
    path('api/tree-group/<int:pk>/', views.TreeGroupDetail.as_view()),
    path('api/harvest/', views.HarvestList.as_view()),
    path('api/harvest/<int:pk>/', views.HarvestDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)