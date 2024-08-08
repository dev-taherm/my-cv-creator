from django.db import models


class Experience(models.Model):
    profile = models.ForeignKey(
        "portfolio.Profile",
        on_delete=models.CASCADE,
    )

    title = models.CharField(
        max_length=100,
    )

    company = models.CharField(
        max_length=100,
    )

    description = models.TextField()

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.title} - {self.profile.user.username}"

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"
