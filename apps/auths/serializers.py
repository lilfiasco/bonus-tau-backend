from django.http import Http404
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password

from auths.models import CustomUser


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Сериализатор для создания токена авторизации."""

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['phone'] = user.phone

        return token


class UserRegisterSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации пользователя."""

    phone = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True
    )

    class Meta:
        model = CustomUser
        fields = (
            'name', 'surname', 'phone', 'password', 'password2'
        )
        extra_kwargs = {
            'name': {'required': True},
            'surname': {'required': True},
            'phone': {'required': True},
        }

    def validate_passwords(self, attrs, password2):
        if attrs['password'] != password2:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})
        return attrs

    def validate_phone(self, value):
        if CustomUser.objects.filter(phone=value).exists():
            raise serializers.ValidationError("Пользователь с таким номером телефона уже существует.")
        return value

    def create(self, validated_data):
        password2 = validated_data.pop('password2')
        self.validate_passwords(validated_data, password2)

        user = CustomUser.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])

        user.save()

        return user
    

class UserMeSerializer(serializers.ModelSerializer):
    """UserSerializer."""

    class Meta:
        model = CustomUser
        fields = [
            'name',
            'surname',
            'phone'
        ]
