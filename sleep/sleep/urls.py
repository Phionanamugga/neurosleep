"""
URL configuration for sleep project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import RedirectView
from sleep import views as sleep_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("sleep.api_urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", sleep_views.signup, name="signup"),
    path("", sleep_views.dashboard, name="dashboard"),
    path("sessions/", sleep_views.session_list, name="session_list"),
    path("sessions/new/", sleep_views.session_create, name="session_create"),
    path("sessions/<int:pk>/edit/", sleep_views.session_edit, name="session_edit"),
    path("goals/", sleep_views.goal_view, name="goal_view"),
    path("import/", sleep_views.import_csv, name="import_csv"),
    path("export/", sleep_views.export_csv, name="export_csv"),
]
