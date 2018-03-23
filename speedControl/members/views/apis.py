from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import AccessTokenLoginSerializer, UserSerializer


class FacebookLogin(APIView):
    def post(self, request):
        serializer = AccessTokenLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)

        data = {
            'token': token.key,
            'user': UserSerializer(user).data
        }
        return Response(data)


class FacebookUserGetInfo(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get(self, request):
        print(request.user)
        serializer = UserSerializer(request.user)
        data = {
            'user': serializer.data
        }
        return Response(data)
