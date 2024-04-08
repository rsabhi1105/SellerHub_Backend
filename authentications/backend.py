# from django.contrib.auth.backends import ModelBackend
#
# from authentications.models import User
#
#
# class PhoneBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             user = User.objects.get(phone_number=username)
#         except User.DoesNotExist:
#             return None
#         else:
#             if user.check_password(password):
#                 return user
#         return None
