from django.urls import path
from .views import SubjectsListView,TeachersListView,SubjectsEntryView,TeachersEntryView

urlpatterns = [
    path('subjects', SubjectsListView.as_view(), name='subjects_list'),
    path('teachers', TeachersListView.as_view(), name='teachers_list'),
    path('subjects/entry', SubjectsEntryView.as_view(), name='subjects_entry'),
    path('teachers/entry', TeachersEntryView.as_view(), name='teachers_entry'),
]

