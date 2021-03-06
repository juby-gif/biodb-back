from django.http import HttpResponse, JsonResponse
from rest_framework import views, response, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from api.serializers import UpdateSerializer
from foundation.models import AppleHealthKitDataDB


class UserprofileRetrieveAPI(views.APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def get(self,request):
        return response.Response(
            status = status.HTTP_200_OK,
            data = {
             'first_name': request.user.first_name,
             'last_name': request.user.last_name,
             'email': request.user.email,
             'username': request.user.username,
             # 'date_of_birth': request.user.date_of_birth,
             # 'blood_type': request.user.blood_type,
        })

class UserprofileUpdateAPI(views.APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def put(self,request):
        serializer = UpdateSerializer(request.user, data=request.data, context={
            'request' : request,
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response(
            status=status.HTTP_200_OK,
            data={
                'Updation Status': "Succesfully Updated",
                'Updated data': serializer.data,
            }
        )
