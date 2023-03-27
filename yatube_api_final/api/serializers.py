from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from .models import Post, Comment, Follow, Group

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Post
        fields = ('__all__')
        read_only_fields = ('pub_date',)
        extra_kwargs = {
            'author': {'read_only': True},
            'text': {'required': True}
        }

    def create(self, validated_data):
        author = self.context['request'].user

        validated_data['author'] = author

        post = Post.objects.create(**validated_data)
        post.save()

        return post


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        fields = ('__all__')
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['user', 'author']
        model = Follow


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group
