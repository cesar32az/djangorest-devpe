from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.users.api.serializers import UserSerializer
from apps.users.models import User

@api_view(['GET', 'POST'])
def user_api_view(request):

    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many = True)
        return Response(users_serializer.data)

    elif request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)


"""
#from rest_framework.views import APIView 

class UserAPIView(APIView):

    def get(self, request):

        users = User.objects.all()
        users_serializer = UserSerializer(users, many = True)
        return Response(users_serializer.data) 
"""