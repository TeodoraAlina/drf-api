from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField('owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField('owner.profile.id')
    profile_image = serializers.ReadOnlyField('owner.profile.image.url')

    def validate_image(self, value):
        if value_size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields: [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'created_at', 'image', 'updated_at', 'titile', 'content',
            'image_filter'
        ]
