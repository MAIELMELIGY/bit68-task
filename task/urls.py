from django.urls import path

from task.views import ProductListcreate ,Listproduct 
urlpatterns=[
    path("productlistcreate/",ProductListcreate.as_view(),name="productlistcreate"),
    path("Listproduct/",Listproduct.as_view(),name="Listproduct"),
]