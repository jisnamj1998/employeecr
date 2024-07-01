from django.urls import path

from myapp import views 

urlpatterns=[
             path("employee/list/",views.EmployeeListView.as_view(),name="employee-list"),
             path("employee/create/",views.EmployeeCreateView.as_view(),name="employee-create"),
             path("employee/<int:pk>/",views.EmployeeDetailView.as_view(),name="employee-detail"),
             path("employee/<int:pk>/remove",views.EmployeeDeleteView.as_view(),name="employee-delete"),
             path("employee/<int:pk>/change",views.EmployeeUpdateView.as_view(),name="employee-update"),
            ]
