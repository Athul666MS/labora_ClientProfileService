from django.urls import path
from profiles import views
from profiles.views import InternalClientListView

urlpatterns = [
    path("client/add/", views.client_profile_add),
    path("client/update/", views.client_profile_update),
    path("client/view/", views.client_profile_view),
    path("client/delete/", views.client_profile_delete),

    path(
        "internal/clients/",
        InternalClientListView.as_view()
    ),


]
