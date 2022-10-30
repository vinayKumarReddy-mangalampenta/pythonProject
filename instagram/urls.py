from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("projects/", include('project.urls')),
    path("api/", include('APIs.urls')),
    path("", include('users.urls')),
    path('change-password/', auth_views.PasswordChangeView.as_view(),
         name='PasswordChangeView'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="passwordReset.html"),
         name='password_reset'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name="passwordResetDone.html"),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="passwordResetConfirmation.html"),
         name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="passwordResetComplete.html"),
         name='password_reset_complete')
]
