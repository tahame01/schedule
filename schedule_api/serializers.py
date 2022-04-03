
from rest_framework import serializers
from .models import Subjects, Teachers

class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ('subject_id', 'subject_name', 'subject_weight')


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ('teacher_id','teacher_name', 'teaching_subjects')