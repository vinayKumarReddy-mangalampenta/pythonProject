from django.contrib.auth.models import User 

from rest_framework import serializers
from project.models import Project, Tag, Review
from users.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User 
        fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):
    # user = UserSerializer(many=False)
    class Meta:
        model = Profile
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False)
    class Meta:
        model = Review
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False)
    tags = TagSerializer(many=True)
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data
