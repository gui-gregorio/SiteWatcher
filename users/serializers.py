from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "email", "name", "number", "password"]
        extra_kwargs = {
            'password': {"write_only": True}
        }
    
    def create(self, validated_data):
        email = validated_data["email"]
        name = validated_data["name"]
        number = validated_data["number"]
        password = validated_data["password"]

        user = get_user_model()
        new_user = user.objects.create(email=email, name=name, number=number)
        new_user.set_password(password)
        new_user.save
        return new_user
