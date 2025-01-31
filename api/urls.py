from django.urls import path

from api import views 

urlpatterns=[
    path("employees/",views.EmployeeListCreateView.as_view()),
    path("employees/<int:pk>/",views.EmployeeRetrieveUpdateDeleteView.as_view()),
    path("employees/department/",views.DepartmentView.as_view()),
]

