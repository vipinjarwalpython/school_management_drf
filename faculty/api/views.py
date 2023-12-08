from faculty.models import Faculty
from faculty.api.serializer import FacultySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class FacultyAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id=None):
        try:
            if id is not None:
                fac = Faculty.objects.get(pk=id)
                serialzer = FacultySerializer(fac)
                return Response(serialzer.data)

            fac = Faculty.objects.all()
            serialzer = FacultySerializer(fac, many=True)
            return Response(serialzer.data)

        except Exception as E:
            return Response(str(E), status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            serialzer = FacultySerializer(data=request.data)
            if serialzer.is_valid():
                serialzer.save()
                return Response({"msg": "Data Created"}, status=status.HTTP_201_CREATED)
            return Response(serialzer._errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as E:
            return Response(str(E), status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        try:
            fac = Faculty.objects.get(pk=id)
            serilazer = FacultySerializer(fac, data=request.data)
            if serilazer.is_valid():
                serilazer.save()
                return Response({"msg": "Complete Data Updated"})
            return Response(serilazer._errors)

        except Exception as E:
            return Response(str(E), status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        try:
            fac = Faculty.objects.get(pk=id)
            serializer = FacultySerializer(fac, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Partially Data Updated"})
            return Response(serializer._errors)

        except Exception as E:
            return Response(str(E), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        try:
            fac = Faculty.objects.get(pk=id)
            fac.delete()
            return Response({"msg": "Data Deleted"})

        except Exception as E:
            return Response(str(E), status=status.HTTP_400_BAD_REQUEST)
