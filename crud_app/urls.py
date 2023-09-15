from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'crud_app'

urlpatterns = [
    path('', views.view_all_persons, name='view_all_persons'),
    path('api/', views.crud_person_profile_by_firstname, name='crud_person_profile_by_firstname'),
    path('api/<int:user_id>', views.read_edit_delete_person_profile_by_id, name='read_edit_delete_person_profile_by_id'),

]

