from rest_framework import serializers
from .models import ClientProfile


class ClientProfileViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = "__all__"
        # read_only_fields = (
        #     "user_id",
        #     "is_verified",
        #     "is_active",
        #     "created_at",
        #     "updated_at",
        #     "last_seen",
        #     "total_jobs_completed",
        #     "average_rating",
        # )
