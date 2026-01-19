from django.urls import path
from profiles import views


urlpatterns = [
    path("profile/add/", views.client_profile_add),
    path("profile/update/", views.client_profile_update),
    path("profile/view/", views.client_profile_view),
    path("profile/delete/", views.client_profile_delete),
]
