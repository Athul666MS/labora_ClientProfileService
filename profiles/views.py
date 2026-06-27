from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .role_permissions import IsClient
from .serializers import ClientProfileViewSerializer, InternalClientListSerializer
from .models import ClientProfile
from rest_framework.views import APIView
from rest_framework.response import Response

from .permissions.internal_service import (
    IsInternalService
)
from .models import ClientProfile
from .serializers import ClientProfileViewSerializer

@api_view(["POST"])
@permission_classes([IsAuthenticated, IsClient])
def client_profile_add(request):
    try:
        data = request.data.copy()
        data["user_id"] = request.user.id
        serializer = ClientProfileViewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Profile added"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT", "PATCH"])
@permission_classes([IsAuthenticated, IsClient])
def client_profile_update(request):
    user_id = request.user.id

    try:
        profile = ClientProfile.objects.get(user_id=user_id)
    except ClientProfile.DoesNotExist:
        return Response(
            {"error": "Profile not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = ClientProfileViewSerializer(
        instance=profile,
        data=request.data,
        partial=True
    )

    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Profile updated"},
            status=status.HTTP_200_OK
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated, IsClient])
def client_profile_view(request):
    user_id = request.user.id

    try:
        profile = ClientProfile.objects.get(user_id=user_id)
    except ClientProfile.DoesNotExist:
        return Response(
            {"error": "Profile not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = ClientProfileViewSerializer(profile)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated, IsClient])
def client_profile_delete(request):
    user_id = request.user.id

    try:
        profile = ClientProfile.objects.get(user_id=user_id)
    except ClientProfile.DoesNotExist:
        return Response(
            {"error": "Profile not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    profile.delete()
    return Response(
        {"message": "Profile deleted successfully"},
        status=status.HTTP_204_NO_CONTENT
    )



class InternalClientListView(APIView):
    authentication_classes = []
    permission_classes = [IsInternalService]

    def get(self, request):

        clients = ClientProfile.objects.all().order_by("-created_at")

        paginator = PageNumberPagination()
        paginator.page_size = 20

        page = paginator.paginate_queryset(
            clients,
            request
        )

        serializer = InternalClientListSerializer(
            page,
            many=True
        )

        return paginator.get_paginated_response(
            serializer.data
        )