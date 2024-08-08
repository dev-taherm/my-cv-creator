from django.urls import path

from portfolio.views import CreateProfileView, DashboardView, UpdateProfileView


urlpatterns = [
    path(
        "",
        DashboardView.as_view(),
        name="dashboard",
    ),
    path(
        "edit-profile/",
        UpdateProfileView.as_view(),
        name="edit_profile",
    ),
    path(
        "create-profile/",
        CreateProfileView.as_view(),
        name="create_profile",
    ),
]
