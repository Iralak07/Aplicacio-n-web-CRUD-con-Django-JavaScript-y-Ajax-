from django.urls import path
from core.admin_post.views import (
    DashBoardView,
    ListCategoryView,
)

app_name = 'admin_post'


urlpatterns = [
    # Dashboard
    path('dashboard/', DashBoardView.as_view(),name='dashboard'),
    
    # Categorias
    path('listCategory/', ListCategoryView.as_view(), name="listCategory"),
]