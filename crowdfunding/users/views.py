from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer,CustomUserDetailSerializer,CustomUserActivitySerializer
from rest_framework import permissions, status
from .permissions import OwnProfile



class CustomUserList(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CustomUserDetail(APIView):
    permission_classes = [OwnProfile, permissions.IsAuthenticatedOrReadOnly]
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        user = self.get_object(pk)
        self.check_object_permissions(request, user)
        serializer = CustomUserDetailSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        self.check_object_permissions(request, user)
        data = request.data
        serializer = CustomUserDetailSerializer(
            instance=user,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    def delete(self, request, pk):
        user = self.get_object(pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomUserActivityDetail(APIView):
    permission_classes = [OwnProfile]
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        user = self.get_object(pk)
        self.check_object_permissions(request, user)
        serializer = CustomUserActivitySerializer(user)
        return Response(serializer.data)



# class PublicProfileAPI(APIView):
#     def get_object(self, pk):
#         try:
#             return PublicProfile.objects.get(pk=pk)
#         except PublicProfile.DoesNotExist:
#             raise Http404
#     def get(self, request, pk):
#         user = self.get_object(pk)
#         self.check_object_permissions(request, user)
#         serializer = PublicProfileSerializer(user)
#         return Response(serializer.data)

# user = get_object_or_404(CustomUser, pk=kwargs['user_id'])