from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status

from .serializers import ClientProfileViewSerializer
from .models import ClientProfile


@api_view(["POST"])
@permission_classes([AllowAny])
def client_profile_add(request):
    try:
        serializer = ClientProfileViewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Profile added"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        print("🔥 ERROR:", e)
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT", "PATCH"])
@permission_classes([AllowAny])
def client_profile_update(request):
    user_id = request.data.get("user_id")

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
@permission_classes([AllowAny])
def client_profile_view(request):
    user_id = request.query_params.get("user_id")

    if not user_id:
        return Response(
            {"error": "user_id is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

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
@permission_classes([AllowAny])
def client_profile_delete(request):
    user_id = request.data.get("user_id")

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
