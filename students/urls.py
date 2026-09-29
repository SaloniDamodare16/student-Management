from django.urls import path
from . import views


urlpatterns = [

    # Home
    path('', views.home, name='home'),

    # Students
    path('students/', views.student_list, name='student_list'),

    path(
        'students/add/',
        views.student_add,
        name='student_add'
    ),

    path(
        'students/edit/<int:id>/',
        views.student_edit,
        name='student_edit'
    ),

    path(
        'students/delete/<int:id>/',
        views.student_delete,
        name='student_delete'
    ),

    # Other pages
    path(
        'about/',
        views.about,
        name='about'
    ),

    path(
        'contact/',
        views.contact,
        name='contact'
    ),
]