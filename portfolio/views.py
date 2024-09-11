from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, CreateView
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from django.contrib.auth import login

from experience.models import Experience
from portfolio.forms import ProfileForm
from portfolio.models import Profile


class DashboardView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        context["profile"] = profile
        context["experiences"] = Experience.objects.filter(profile=profile)
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse_lazy("create_profile"))
        return super().dispatch(request, *args, **kwargs)


class CreateProfileView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = "portfolio/create-profile.html"
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            guest_username = "guest_" + get_random_string(length=10)
            guest_user = User.objects.create_user(
                username=guest_username, password="guestpassword"
            )

            login(self.request, guest_user)
            form.instance.user = guest_user
        else:
            form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateProfileView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "portfolio/edit_profile.html"
    success_url = reverse_lazy("dashboard")

    def get_object(self):
        return Profile.objects.get_or_create(user=self.request.user)[0]
