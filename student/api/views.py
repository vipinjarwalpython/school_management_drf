from django.shortcuts import render
from rest_framework.response import Response
from student.models import Student
from student.api.serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView


class StudentAPI(APIView):
    def get(self, request, id=None):
        try:
            if id is not None:
                stu = Student.objects.get(pk=id)
                serializer = StudentSerializer(stu)
                return Response(serializer.data)

            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            return Response(serializer.data)

        except Exception as E:
            return Response(str(E), status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Data Created"}, status=status.HTTP_201_CREATED)
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as E:
            return Response(str(E), status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        try:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(stu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Complete Data Updated"})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as E:
            return Response(str(E), status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        try:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(stu, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Partial Data Updated"})
            return Response(serializer.errors)

        except Exception as E:
            return Response(str(E), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        try:
            stu = Student.objects.get(pk=id)
            stu.delete()
            return Response({"msg": "Data Deleted"})

        except Exception as E:
            return Response(str(E), status=status.HTTP_400_BAD_REQUEST)

    # return Response({'msg':'Insert Proper Id'})
