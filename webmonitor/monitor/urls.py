from django.urls import path

from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('add_url',views.add_url,name='add-url'),
    path('search_url',views.search_url,name='search-url'),
    path('update_url/<int:web>',views.update_url,name='update_url'),
    path('delete_url/<int:web>',views.delete_url,name="delete_url"),
]