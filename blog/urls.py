from django.urls import path
from .views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView, CustomLoginView, CustomLogoutView, BlogListViewAdmin



app_name='blog'

urlpatterns = [
    path('inicio/', BlogListView.as_view(), name='home'),
    path('adminview/', BlogListViewAdmin.as_view(), name='homeadmin'),
    path('create/', BlogCreateView.as_view(), name="create"),
    path('<int:pk>/', BlogDetailView.as_view(), name="detail"),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name="delete"),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]



