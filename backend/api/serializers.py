from rest_framework import serializers

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)

    def get_active(self):
        return self.user.active