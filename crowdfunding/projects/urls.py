from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('likes/', views.LikeList.as_view()),
    path('projectscreate/', views.ProjectList.as_view()),
    path('projects/', views.ProjectOrderList.as_view()),
    path('projects/<int:pk>', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('pledges/<int:pk>', views.PledgeDetail.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>', views.CategoryDetail.as_view()),
    path('projects/<str:name>/', views.CategoryProject.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)

