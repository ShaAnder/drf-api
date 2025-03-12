from rest_framework import serializers
from posts.models import Post
from reactions import Reaction


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    reaction_id = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                "Image size larger than 2MB!"
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                "Image width larger than 4096px"
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                "Image height larger than 4096px"
            )

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_reaction_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            reaction = Reaction.objects.filter(
                owner=user, post=obj
            ).first()
            return reaction.id if reaction else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'image_filter', 'reaction_id',
        ]
