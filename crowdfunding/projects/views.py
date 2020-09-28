from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project,Pledge,Category, Like
from .serializers import ProjectSerializer,PledgeSerializer,ProjectDetailSerializer,PledgeDetailSerializer,CategorySerializer,CategoryProjectSerializer, LikeSerializer,CategoryDetailSerializer
from django.http import Http404
from rest_framework import status,permissions, generics, filters
from .permissions import IsOwnerOrReadOnly,IsSupporterOrReadOnly,IsAdminUserOrReadOnly
from django.contrib.auth import get_user_model
from django.db.models import Prefetch
from rest_framework import viewsets

#PERFORM CREATE


User = get_user_model()

# Create your views here.
class CategoryList(APIView):
    permission_classes = [IsAdminUserOrReadOnly]
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
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


class CategoryDetail(APIView):
    permission_classes = [permissions.IsAdminUser]    

    def get_object(self,pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        categories = self.get_object(pk)
        serializer = CategorySerializer(categories)
        return Response(serializer.data) 

    def put(self, request, pk):
            categories = self.get_object(pk)
            self.check_object_permissions(request, categories)
            data = request.data
            serializer = CategoryDetailSerializer(
                instance=categories,
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
        categories = self.get_object(pk)
        self.check_object_permissions(request, categories)
        categories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )


class ProjectOrderList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['campaign_end_date', 'owner','proj_cat','date_created']


class ProjectDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)
    
    def put(self, request, pk):
        project = self.get_object(pk)
        self.check_object_permissions(request, project)
        data = request.data
        serializer = ProjectDetailSerializer(
            instance=project,
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
        project = self.get_object(pk)
        self.check_object_permissions(request, project)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    
class PledgeList(APIView):
    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )    

class PledgeDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsSupporterOrReadOnly]
    def get_object(self,pk):
        try:
            return Pledge.objects.get(pk=pk)
        except Pledge.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        pledges = self.get_object(pk)
        serializer = PledgeSerializer(pledges)
        return Response(serializer.data) 

    def put(self, request, pk):
            pledges = self.get_object(pk)
            self.check_object_permissions(request, pledges)
            data = request.data
            serializer = PledgeDetailSerializer(
                instance=pledges,
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
        pledges = self.get_object(pk)
        self.check_object_permissions(request, pledges)
        pledges.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryProject(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryProjectSerializer
    lookup_field = 'name'



class LikeList(APIView):
    def get(self, request):
        likes = Like.objects.all()
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(liker=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )    

