from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project,Pledge,Category
from .serializers import ProjectSerializer,PledgeSerializer,ProjectDetailSerializer,PledgeDetailSerializer,CategorySerializer,CategoryProjectSerializer
from django.http import Http404
from rest_framework import status,permissions, generics
from .permissions import IsOwnerOrReadOnly,IsSupporterOrReadOnly
# Create your views here.

class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)



class CategoryEditList(CategoryList):
    permission_classes = [permissions.IsAdminUser]
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
