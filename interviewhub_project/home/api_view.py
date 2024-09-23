from home.models import *
from home.serializers import *
from utils.decorators import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q


class SignupAPI(APIView):
    def post(self, request, *args, **kwargs):
        try:

            if not request.data.get("username"):
                return Response({"msg" : "Enter user username", "status" : status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
            if not request.data.get("first_name"):
                return Response({"msg" : "Enter user first_name", "status" : status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
            if not request.data.get("last_name"):
                return Response({"msg" : "Enter user last_name", "status" : status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
            if not request.data.get("email"):
                return Response({"msg" : "Enter user email", "status" : status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
            if not request.data.get("mobile_no"):
                return Response({"msg" : "Enter user mobile_no", "status" : status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
            if not request.data.get("state"):
                return Response({"msg" : "Enter user state", "status" : status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
            if not request.data.get("gender"):
                return Response({"msg" : "Enter user gender", "status" : status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
            if not request.data.get("role"):
                return Response({"msg" : "Enter user role", "status" : status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
            if not request.data.get("password"):
                return Response({"msg" : "Enter user password", "status" : status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
            if not request.data.get("confirm_password"):
                return Response({"msg" : "Enter user confirm_password", "status" : status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)


            if request.data.get("password") != request.data.get("confirm_password"):
                return Response({"msg" : "Password doesnt match", "status" : status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)


            user = User.objects.create(username = request.data.get("username"),
                                       first_name = request.data.get("first_name"),
                                       last_name = request.data.get("last_name"),
                                       email = request.data.get("email"),
                                       mobile_no = request.data.get("mobile_no"),
                                       state = request.data.get("state"),
                                       gender = request.data.get("gender"),
                                       role = request.data.get("role"),
                                       password = request.data.get("password"),
                                       is_candidate = request.data.get("is_candidate"),    
            )
            user.set_password(request.data.get("password"))
            user.save()


            return Response({"msg" : "User registered successfully", "status" : status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"msg" : str(e), "status" : status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
        




class LoginAPI(APIView):
    def post(self, request, format = None):
            try:

                if not request.data.get("email"):
                    return Response({"msg" : "Enter email", "status" : status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
                if not request.data.get("password"):
                    return Response({"msg" : "Enter password", "status" : status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)

                user = authenticate(request, email=request.data.get("email"), password=request.data.get("password"))
                
                
                if user is None:
                    return Response({"msg": "Invalid credentials", "status": status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
                    
                    #for decorator
                    # request.user = user  
                    # if not user.is_candidate:
                    #     return Response({"msg": "Only candidates are allowed to login", "status": status.HTTP_403_FORBIDDEN},
                    #                 status=status.HTTP_403_FORBIDDEN)

                if not user.is_active:
                        return Response({"msg" : "Your account is not active",
                                        "status":status.HTTP_400_BAD_REQUEST},
                                        status=status.HTTP_400_BAD_REQUEST)
                    
                login(request, user)

                refresh = RefreshToken.for_user(user)
                access = str(refresh.access_token)

                return Response({"msg" : "User logged in successfully", 
                                "refresh" : str(refresh),
                                "access" : access ,
                                "status" : status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"msg" : str(e), "status" : status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
            




# class UpdateAPI(APIView):
#     permission_classes = [IsAuthenticated]
#     def post(self, request, format=None):
#         try:
        
#             if User.objects.filter(id = request.user.id).exists():
#                 user = User.objects.get(id = request.user.id)

#                 serializer = UserSerializer(user, data=request.data, partial = True )
                
#                 if serializer.is_valid():
#                     serializer.save()
#                     print(user.last_name)
#                 return Response({"msg" : "Data saved",
#                                 "data" : serializer.data, 
#                                 "status" : status.HTTP_200_OK}, status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response({"msg" : str(e), "status" : status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
        



class UpdateAPI(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        try:
        
            if User.objects.filter(id = request.user.id).exists():
                user = User.objects.get(id = request.user.id)

                if request.data.get("first_name"):
                    user.first_name = request.data.get("first_name")
                if request.data.get("last_name"):
                    user.last_name = request.data.get("last_name")
                if request.data.get("username"):
                    user.username = request.data.get("username")
                if request.data.get("email"):
                    user.email = request.data.get("email")
                if request.data.get("mobile_code"):
                    user.mobile_code = request.data.get("mobile_code")
                if request.data.get("mobile_no"):
                    user.mobile_no = request.data.get("mobile_no")
                if request.data.get("age"):
                    user.age = request.data.get("age")
                if request.data.get("gender"):
                    user.gender = request.data.get("gender")
                if request.data.get("profile_pic"):
                    user.profile_pic = request.data.get("profile_pic")
                if request.data.get("state"):
                    user.state = request.data.get("state")
                if request.data.get("role"):
                    user.role = request.data.get("role")
                if request.data.get("social_id"):
                    user.social_id = request.data.get("social_id")
                if request.data.get("social_type"):
                    user.social_type = request.data.get("social_type")             
                
                user.save()
                serializer = UserSerializer(user)
                return Response({"msg" : "Data saved",
                                "data" : serializer.data, 
                                "status" : status.HTTP_200_OK}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"msg" : str(e), "status" : status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
        


class ListUserAPI(APIView):
    def get(self, request, *args, **kwargs):

        # users = User.objects.filter(Q(first_name = "rupam11") | Q(email = "suraj@gmail.com"))
        # users = User.objects.filter(id=2).update(first_name="xx")
        users = User.objects.all()
        print(users.count())
        # serializer = UserSerializer(users, many=True)
        
    
        return Response()