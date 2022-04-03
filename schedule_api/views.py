from rest_framework import generics
from .models import Subjects,Teachers
from .serializers import SubjectsSerializer,TeachersSerializer


class SubjectsListView(generics.ListAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer


class SubjectsEntryView(generics.ListCreateAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer



class TeachersListView(generics.ListAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer

class TeachersEntryView(generics.ListCreateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer