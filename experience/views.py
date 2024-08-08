from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from experience.forms import ExperienceForm
from experience.models import Experience


class CreateExperienceView(CreateView):
    model = Experience
    form_class = ExperienceForm
    template_name = "portfolio/add_experience.html"
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)
