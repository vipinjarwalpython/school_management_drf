from rest_framework import serializers
from faculty.models import Faculty
from django.contrib.auth.models import User


class UserWithFacultySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "username", "email"]


class FacultySerializer(serializers.HyperlinkedModelSerializer):
    faculty = UserWithFacultySerializer()

    class Meta:
        model = Faculty
        fields = ["id", "faculty"]

    # username = serializers.PrimaryKeyRelatedField(
    #     source="faculty.username", queryset=User.objects.all(), many=False
    # )
    # first_name = serializers.PrimaryKeyRelatedField(
    #     source="faculty.first_name", queryset=User.objects.all(), many=False
    # )
    # email = serializers.PrimaryKeyRelatedField(
    #     source="faculty.email", queryset=User.objects.all(), many=False
    # )
