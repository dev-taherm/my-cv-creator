from django.db import models
from django.contrib.auth.models import User


class TemplateChoices(models.TextChoices):
    TEMPLATE1 = "template1", "Template 1"
    TEMPLATE2 = "template2", "Template 2"
    TEMPLATE3 = "template3", "Template 3"


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        max_length=100,
    )

    bio = models.TextField(
        blank=True,
    )

    template_choice = models.CharField(
        max_length=100,
        choices=TemplateChoices.choices,
        default=TemplateChoices.TEMPLATE1,
    )

    def __str__(self):
        return f"{self.name} - {self.user.username}"

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ["user"]
