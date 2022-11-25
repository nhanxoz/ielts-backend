from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers
from django.contrib.auth import authenticate
from .validators import validate_username
import time

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    model = Account
    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])

        if not user:
            raise serializers.ValidationError('Incorrect email or password.')

        if not user.is_active:
            raise serializers.ValidationError('User is disabled.')

        return {'user': user}


class ChangePasswordSerializer(serializers.Serializer):
    model = Account

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = (
            
            'username',
            'image',
            'createdtime',
            'idgroup',
            'password',
            
        )
        read_only_fields = ('createdtime', 'idgroup',)
        extra_kwargs = {
            'password': {'required': True, 'write_only': True},
            'username': {'required': True}
        }
    def create(self, validated_data):
        user = super().create(validated_data)
        
        user.set_password(validated_data['password'])
        user.save()
        return user
    @staticmethod
    def validate_email(value):
        return validate_username(value)


class AccountsSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", "username", "idgroup", "createdtime", "image"]

class AnswersSerializer(ModelSerializer):
    class Meta:
        model=Answer
        fields = ["id", "content"]

class CertificatesSerializer(ModelSerializer):
    class Meta:
        model=Certificate
        fields =["id", "image", "band", "l", "r", "w", "s", "name", "time"]

class CommentsSerializer(ModelSerializer):
    class Meta:
        model=Comment
        fields=["id", "accountid", "createtime", "supercommentid", "postid", "vote", "downvote"]

class CoursesSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "name", "description", "startdate", "createdate", "roomid"]

class EssayquestionsSerializer(ModelSerializer):
    class Meta:
        model = Essayquestion
        fields = ["id", "content", "description", "information", "displayorder", "createdtime"]

class ExamsSerializer(ModelSerializer):
    class Meta:
        model = Exam
        fields = ["id", "createddate", "questions", "type", "idcourse"]
    
class PostsSerializer(ModelSerializer):
    class Meta:
        model = Post 
        fields = ["id", "title", "content", "vote", "downvote", "authorid"]

class QuestionsSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "content", "subquestions", "examid", "audiofile", "imagefile"]
class StudentsSerializer(ModelSerializer):
    class Meta:
        model = Student 
        fields = ["id", "fullname", "level", "dob" , "startdate", "phonenumber", "image", "email", "currentcourse", "learnedcourse"]
    def create(self, validated_data):
        validated_data['accountid'] = self.context['request'].user
        return super(StudentsSerializer, self).create(validated_data)
class TeachersSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["id", "fullname", "ieltscertificate", "dob", "startdate", "phonenumber", "image", "address", "billing_account", "billing_bank", "email", "note", "taughtcourse","accountid"]
class SubquestionsSerializer(ModelSerializer):
    class Meta:
        model = Subquestion
        fields = ["id", "content", "questiontype", "questionid"]
class ReportperlessonsSerializer(ModelSerializer):
    class Meta:
        model = Reportperlesson
        fields = ["id", "studentid", "teacherid", "isabsent_field", "reasonabsent", "comment", "scorehomework", "courseid"]
