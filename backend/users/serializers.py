from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from backend.users.models import CustomUser
from django.contrib.auth.password_validation import validate_password


class CustomUserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=CustomUser.objects.all(),
            )
        ],
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={
            "input_type": "password",
        },
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={
            "input_type": "password",
        },
    )

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "password",
            "password2",
            "first_name",
            "last_name",
            "is_staff",
            "is_active",
            "date_joined",
        ]
        read_only_fields = ("id",)

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {
                    "password": "Passwords must match",
                }
            )
        return attrs

    def create(self, validate_data):
        user = CustomUser.objects.create_user(
            email=validate_data["email"],
        )
        user.set_password(
            validate_data["password"],
        )
        user.save()
        return user
