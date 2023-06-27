import email
from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


#Dr-Register-Serializer..
class DoctorRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            "doctor_id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "specialty",
            "qualifications",
            "address",
            "gender",
            "date_of_birth",
            "image",
        ]

        def validate(self, attrs):
            email = attrs.get("email")
            if Doctor.objects.filter(email=email).exists():
                raise serializers.ValidationError("This email already exists.")
            return attrs

    def create(self, validated_data):
        return Doctor.objects.create(**validated_data)


#Dr-AllDetails-Serializer..

class DoctorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            "doctor_id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "specialty",
            "qualifications",
            "address",
            "gender",
            "date_of_birth",
            "image",
        ]


# update Doctor Details...
class DoctorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "specialty",
            "qualifications",
            "address",
            "gender",
            "date_of_birth",
            "image",
        ]
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance



#dr-search by name query..

class DoctorSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields = [
            "doctor_id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "specialty",
            "qualifications",
            "address",
            "gender",
            "image",
        ]




# @get Toatl Count doctor api
class TotalDoctorCountSerializer(serializers.Serializer):
    total_count = serializers.IntegerField()