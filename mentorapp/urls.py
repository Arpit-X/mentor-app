"""summerMRND URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views.college import *
from .forms.auth import *
from .views.serialiser_views import *
app_name = "mentorApp"

urlpatterns = [
    path("colleges/",CollegeListView.as_view(), name="college_html"),
    path("colleges/add/", CreateAddCollegeView.as_view(), name="addCollegeForm"),
    path("colleges/<int:id>/",CollegeWiseStudentListView.as_view(),name="college_wise_student_list"),
    path("colleges/<str:acronym>/",CollegeWiseStudentListView.as_view(),name="college_wise_student_list"),
    path("colleges/<int:id>/add",CreateStudentView.as_view(),name="AddStudent"),
    path("colleges/<int:pk>/edit",UpdateCollege.as_view(),name="EditCollege"),
    path("colleges/<int:pk>/delete",DeleteCollege.as_view(),name="DeleteCollege"),
    path("colleges/<int:pk>/student/edit",UpdateStudent.as_view(),name="UpdateStudent"),
    path("colleges/<int:pk>/student/delete",DeleteStudent.as_view(),name="DeleteStudent"),
    path("signup/",SignUpFormView.as_view(),name="signUpform"),
    path("login/",LoginFormView.as_view(),name="loginForm"),
    path("logout/",LogOut.as_view(),name="logOut"),
    path("api/colleges/",college_list),
    path("api/colleges/<int:pk>",college_detail),
    path("api/colleges/<int:cid>/students/",StudentList.as_view()),
    path("api/students/all",StudentsCompleteData.as_view()),
    path("api/colleges/<int:cid>/students/<int:pk>",StudentDetails.as_view())
]
