from profiles.models import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated



class EmployerProfileAPI(APIView):
    permission_classed = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        try:

            if not request.data.get("hiring_for"):
                return Response({"msg" : "Enter user hiring_for", "status" : status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)

            if not request.data.get("pan_number"):
                return Response({"msg" : "Enter user pan_number", "status" : status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)

            if not request.data.get("official_email"):
                return Response({"msg" : "Enter user official_email", "status" : status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
            
            if not request.data.get("address"):
                return Response({"msg" : "Enter user company_address", "status" : status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
        
            if not request.data.get("city"):
                return Response({"msg" : "Enter user city", "status" : status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
            
            if not request.data.get("state"):
                return Response({"msg" : "Enter user state", "status" : status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
            
            if not request.data.get("pin_code"):
                return Response({"msg" : "Enter user pin_code", "status" : status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
            
            if not request.data.get("country"):
                return Response({"msg" : "Enter user country", "status" : status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
            
            

            employer = Employer.objects.create(user = request.user,
                                        hiring_for = request.data.get("hiring_for"),
                                        pan_number = request.data.get("pan_number"),
                                        official_email = request.data.get("official_email").lower(),
                                        address = request.data.get("address"),
                                        city = request.data.get("city"),
                                        state = request.data.get("state"),
                                        pin_code = request.data.get("pin_code"),
                                        country = request.data.get("country"),                      
                )
          
            return Response({"msg" : "Profile updated successfully", "status" : status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"msg" : str(e), "status" : status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
        