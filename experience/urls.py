from django.urls import path

from experience.views import CreateExperienceView

urlpatterns = [
    path(
        "add-experience/",
        CreateExperienceView.as_view(),
        name="add_experience",
    ),
]
