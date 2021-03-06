from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import admin
from .views import *

app_name = 'coastalapp'

urlpatterns = [
     path('admin/', admin.site.urls),
     path(
     'admin/password_reset/',
     auth_views.PasswordResetView.as_view(),
     name='admin_password_reset',
     ),
     path(
     'admin/password_reset/done/',
     auth_views.PasswordResetDoneView.as_view(),
     name='password_reset_done',
     ),
     path(
     'reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(),
     name='password_reset_confirm',
     ),
     path(
     'reset/done/',
     auth_views.PasswordResetCompleteView.as_view(),
     name='password_reset_complete',
     ),
     path('', home, name='home'),
     path('accounts/', include('django.contrib.auth.urls')),
     path('logout/', logout_user, name='logout'),
     path('employees/', employee_list, name='employee_list'),
     path('employees/<int:employee_id>/', employee_details, name='employee'),
     path('employees/employee_form', employee_form, name='employee_form'),
     path('employees/<int:employee_id>/employee_form/',
     employee_edit_form, name='employee_edit_form'),
     path('departments/form', department_form, name='department_form'),
     path('departments/<int:department_id>',
     department_details, name='department'),
     path('departments/', department_list, name='department_list'),
     path('jobs/', job_list, name='job_list'),
     path('jobs/past', job_past, name='job_past'),
     path('jobs/<int:job_id>/',
     job_details, name='job'),
     path('jobs/job_form', job_form, name='job_form'),
     path('jobs/<int:job_id>/job_form/',
     job_edit_form, name='job_edit_form'),
     path('vehicles/form', vehicle_form, name='vehicle_form'),
     path('vehicles/', vehicle_list, name='vehicle_list'),
     path('vehicles/<int:vehicle_id>/', vehicle_details, name='vehicle'),
     path('vehicles/<int:vehicle_id>/vehicle_form/',
     vehicle_edit_form, name='vehicle_edit_form')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)