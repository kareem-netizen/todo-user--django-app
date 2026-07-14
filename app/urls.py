from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("", views.task_list, name="task_list"),
    path("create/", views.create_task, name="create_task"),
    path("update/<int:id>/", views.update_task, name="update_task"),
    path("delete/<int:id>/", views.delete_task, name="delete_task"),
]