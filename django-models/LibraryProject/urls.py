from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from relationship_app import views  # import your custom register view

urlpatterns = [
    path("admin/", admin.site.urls),

    # 🔹 Authentication
    path("register/", views.register_view, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),

    # 🔹 App URLs
    path("relationship_app/", include("relationship_app.urls")),
]
