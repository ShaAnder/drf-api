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
        if obj.user_profile.image:
            return obj.user_profile.image.url
        return None