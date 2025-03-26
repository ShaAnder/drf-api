from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='user_profile.id')  
    profile_image = serializers.SerializerMethodField()  

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )

    def get_profile_image(self, obj):
        image = obj.user_profile.image
        # If image is a File/Image instance with a .url attribute, return that.
        if hasattr(image, 'url'):
            return image.url
        # Otherwise, assume it's already a URL or a string.
        return image