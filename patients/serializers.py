from rest_framework import serializers
from patients.models import Patient


# for pateint Register
class PatientRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


# for Pateint Listing....
class PatientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            "patient_id",
            "name",
            "email",
            "phone",
            "age",
            "dob",
            "gender",
            "address",
        ]


# for Pateint Listing By id....
class PatientListIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            "name",
            "email",
            "phone",
            "age",
            "dob",
            "gender",
            "address",
        ]


# for Pateint updatePrfile put/patch By id....
class PatientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            "name",
            "email",
            "phone",
            "age",
            "dob",
            "gender",
            "address",
        ]

    # update method..
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


# -- for Pateint Profile Searching By Query.....
class PatientSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"



# @get Toatl Count doctor api
class TotalPatientCountSerializer(serializers.Serializer):
    total_count = serializers.IntegerField()






#increase Patients @pi..from django.db.models import F

''' 
class PatientIncreaseSerializer(serializers.Serializer):
    increase_percentage = serializers.DecimalField(max_digits=5, decimal_places=2)
    
    def validate_increase_percentage(self, value):
        if value <= 0:
            raise serializers.ValidationError("Increase percentage must be greater than zero.")
        return value
    
    def to_representation(self, instance):
        return {
            'current_patients': instance['current_patients'],
            'increase_percentage': instance['increase_percentage'],
            'increase_amount': instance['increase_amount'],
            'new_total_patients': instance['new_total_patients']
        }
    
    def create(self, validated_data):
        increase_percentage = validated_data['increase_percentage']
        
        current_patients = Patient.objects.count()
        increase_amount = int(current_patients * increase_percentage / 100)
        new_total_patients = current_patients + increase_amount
        
        return {
            'current_patients': current_patients,
            'increase_percentage': increase_percentage,
            'increase_amount': increase_amount,
            'new_total_patients': new_total_patients
        }
'''