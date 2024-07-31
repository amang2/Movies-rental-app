from django.db.models import fields
from rest_framework import serializers
from users.models import UserProfile
from django.contrib.auth.hashers import make_password





class UserProfileSerializer(serializers.ModelSerializer):
    public_id= serializers.CharField(read_only=True)
    user_type= serializers.ChoiceField(choices=["Admin","Customer"])
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model=UserProfile
        fields = ("public_id","username","password","phone_no","user_type")

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.password = make_password(validated_data.pop('password'))
        return super().update(instance, validated_data)

