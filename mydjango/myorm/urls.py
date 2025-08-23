from django.urls import path

from . import views


urlpatterns = [
    path("author", views.AuthorView.as_view(), name="author"),
    # path("user", views.UserView.as_view(), name="user"),
    # path("student", views.StudentView.as_view(), name="student"),
    # path("course", views.CourseView.as_view(), name="course")
]
