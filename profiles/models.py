from django.db import models

class ClientProfile(models.Model):
    # Comes from Auth/User Service (JWT)
    user_id = models.IntegerField(unique=True)

    # Basic Info
    company_name = models.CharField(max_length=200, blank=True)
    full_name = models.CharField(max_length=150)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    profile_image = models.ImageField(
        upload_to="client_profiles/",
        blank=True,
        null=True
    )

    # Business Details
    industry = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)

    # Stats (optional but useful)
    total_jobs_posted = models.PositiveIntegerField(default=0)
    total_spent = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00
    )

    # Meta
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ClientProfile(user_id={self.user_id})"
