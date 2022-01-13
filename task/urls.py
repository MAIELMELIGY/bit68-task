from django.urls import path

from task.views import ProductList 
urlpatterns=[
    path("productlist/",ProductList.as_view(),name="productlist")
]