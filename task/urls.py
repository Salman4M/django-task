from django.urls import path

from task import views

urlpatterns = [
    path('owndetail/<int:id>/',views.owner_detail_view,name='owndetail'),
    path('gallerydet/<int:id>/',views.gallery_view,name='galdetail'),

]
