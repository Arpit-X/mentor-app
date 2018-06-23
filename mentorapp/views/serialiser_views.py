
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pip._vendor.idna import unicode
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from onlineapp.models import College ,Student
from mentorapp.serialisers import *
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework import status,permissions,mixins,generics
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
import base64



@api_view(['GET','POST'])
@authentication_classes((SessionAuthentication,BasicAuthentication))
@permission_classes((IsAuthenticated,))
def college_list(request):
    """
    list of colleges , add college
    """
    if request.method == "GET":
        colleges = College.objects.all()
        serialisers =CollegeSerialiser(colleges,many=True)
        return Response(serialisers.data)

    elif request.method == "POST" :
        data =JSONParser().parse(request)
        serialisers=CollegeSerialiser(data=data)
        if serialisers.is_valid():
            serialisers.save()
            return Response(serialisers.data,status=status.HTTP_201_CREATED)
    return JsonResponse(serialisers.errors,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes((SessionAuthentication,BasicAuthentication))
@permission_classes((IsAuthenticated,))
def college_detail(request, pk):
    """
    retrive update or delelte the college
    """
    try:
        colleges = College.objects.get(id=pk)
    except :
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        serialiser = CollegeSerialiser(colleges)
        return  Response(serialiser.data)

    elif request.method  == 'PUT':
        data = JSONParser().parse(request)
        serialiser = CollegeSerialiser(colleges, data=data)
        if serialiser.is_valid():
            serialiser.save()
            return JsonResponse(serialiser.data)
        return JsonResponse(serialiser.errors,status=300)

    elif request.method == 'DELETE':
        colleges.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class StudentList(generics.ListCreateAPIView):
    serializer_class = StudentsSerialiser
    authentication_classes = {SessionAuthentication,BasicAuthentication}
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        return Student.objects.filter(college__id=self.kwargs['cid'])

    def post(self, request, *args, **kwargs):
        self.request.data['college']= self.kwargs['cid']
        return self.create(request, *args, **kwargs)


class StudentsCompleteData(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentAllDetails

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetails

    def get_queryset(self):
        return Student.objects.filter(college__id=self.kwargs['cid'])
