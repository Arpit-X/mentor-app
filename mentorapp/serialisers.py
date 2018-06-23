from onlineapp.models import *
from rest_framework import serializers


class CollegeSerialiser(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    location = serializers.CharField()
    acronym = serializers.CharField()
    contact = serializers.EmailField()

    def create(self, validated_data):
        return College.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('title', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.acronym = validated_data.get('acronym', instance.acronym)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.save()

        return instance


class MocKtestSerialiser(serializers.ModelSerializer):
    class Meta:
        model= MockTest1
        fields = ('problem1', 'problem2', 'problem3', 'problem4', 'total')


class StudentsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'email', 'db_folder','college')


class StudentAllDetails(serializers.ModelSerializer):
    mocktest1 = MocKtestSerialiser()
    college = CollegeSerialiser()

    class Meta:
        model = Student
        fields = ('id','name', 'email', 'db_folder', 'mocktest1', 'college')


class StudentDetails(serializers.ModelSerializer):
    mocktest1 = MocKtestSerialiser()

    class Meta:
        model = Student
        fields =('id','name', 'email', 'db_folder', 'mocktest1')