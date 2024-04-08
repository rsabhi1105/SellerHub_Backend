from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from authentications.models import User
from authentications.serializer import RegistrationSerializer, LoginSerializer, ForgetPasswordSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from authentications.utils import send_activation_email, reset_pass_link


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegistrationView(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = RegistrationSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            if User.objects.filter(email=email).exists():
                return Response({
                    "status": "error",
                    "message": "Email already exists"
                }, status=status.HTTP_400_BAD_REQUEST)
            user = serializer.save()
            return Response({
                "status": "ok",
                "message": "User registered successfully"
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "status": "error",
                "message": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request):
        user = User.objects.all()
        serializer = LoginSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, requset):
        serializer = LoginSerializer(data=requset.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            # https: // docs.djangoproject.com / en / 4.2 / topics / auth / default /  # user-objects
            user = authenticate(email=email, password=password)
            if user is not None:
                user_id = user.id
                user_email = user.email
                token = get_tokens_for_user(user)
                send_activation_email(user_email, "token")
                user.save()
                return Response({
                    "status": "ok",
                    "message": "user login",
                    "token": token,
                    "user_id": user_id,
                    "user_email": user_email},
                    status=status.HTTP_200_OK)
            else:
                return Response({
                    "status": "error",
                    "message": "invalid email id or password"
                }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ForgetPasswordView(APIView):
    def post(self, request):
        if "email" not in request.data:
            return Response({
                "status": "email_is_not_send"
            }, 400)
        if User.objects.filter(email=request.data["email"]).exists():
            user = User.objects.get(email=request.data["email"])
            uid = user.id
            token = default_token_generator.make_token(user)
            reset_link = f"http://127.0.0.1:8000/user/api/reset_pass/{uid}/{token}"
            reset_pass_link(request.data["email"], reset_link)
            return Response({"msg": "email_sent for password reset"}, 201)
        return Response({"msg": "user does not exist"})


class ResetPassword(APIView):
    def post(self, request, uid, token):
        if not token:
            return Response({"status": "Token field is required"}, status=400)

        try:
            user = User.objects.get(id=uid)
        except User.DoesNotExist:
            return Response({"status": "User not found"}, status=404)

        if not default_token_generator.check_token(user, token):
            return Response({"status": "Your token has expired or is incorrect"}, status=400)

        new_pass = request.data.get("new_password")
        if not new_pass:
            return Response({"status": "New password is required"}, status=400)

        user.set_password(new_pass)
        user.save()

        return Response({"status": "Password updated successfully"}, status=200)
