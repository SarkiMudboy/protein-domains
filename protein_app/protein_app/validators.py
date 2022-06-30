from rest_framework import serializers

def unique_validator(value, field, queryset):

    if value in queryset:
        raise serializers.ValidationError('Protein with this protein id exixts')

    return value