from django.urls import path
from .import views

urlpatterns = [

    path('', views.home, name=''),



    # ---------- Register a user  ---------- #
    # -------------------------------------- #

    path('register', views.register, name='register'),



    # ---------- Login a user  ---------- #
    # ------------------------------------#

    path('my-login', views.my_login, name='my-login'),



    # ------------ Dashboard  page------------ #
    # -----------------------------------------#

    path('dashboard', views.dashboard, name='dashboard'),



    # ------------ PROFILE MANAGEMENT ------------ #
    # ---------------------------------------------#

    path('profile-management', views.profile_management, name='profile-management'),







    # ------------ CREATE A TASK ------------ #
    # ----------------------------------------#

    path('create-task', views.createTask, name='create-task'),




    # ------------ READ A TASK ------------ #
    # ----------------------------------------#

    path('view-tasks', views.viewTask, name='view-tasks'),

   

   
    # ------------ UPDATE A TASK ------------ #
    # ----------------------------------------#

    path('update-task/<str:pk>/', views.updateTask, name='update-task'),




    # ------------ DELETE A TASK ------------ #
    # ----------------------------------------#

    path('delete-task/<str:pk>/', views.deleteTask, name='delete-task'),



    # ---------- Logout a user  ---------- #
    # -------------------------------------#

    path('user-logout', views.user_logout, name='user-logout'),


]










