from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import HRRegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
from ..models import HR


class HRRegisterView(APIView):
    def post(self, request):
        serializer = HRRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'username': user.username,
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class HRTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        
        try:
            hr = self.user.hr
        except HR.DoesNotExist:
            raise AuthenticationFailed("Only HRs are allowed to log in.")

        
        data['username'] = self.user.username
        data['department'] = hr.department

        return data

class HRLoginView(TokenObtainPairView):
    serializer_class = HRTokenObtainPairSerializer
