from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('',views.index, name='index'),
    path('company/',views.company, name='company'),
    path('branch/',views.branch, name='branch'),
    path('branch/create/', views.branch_create, name='branch_create'),
    path('branch/update/<int:pk>/',views.branch_update, name='branch_update'),
    path('branch/delete/<int:pk>/',views.branch_delete, name='branch_delete'),
    path('staff/',views.staff, name='staff'),
    path('employee/',views.employee, name='employee'),
    path('employee/create/', views.employee_create, name='employee_create'),
    path('employee/delete/<int:pk>/',views.employee_delete, name='employee_delete'),
    path('employee/update/<int:pk>',views.employee_update, name='employee_update'),
    path('employee/additional/<int:pk>',views.employee_additional, name='employee_additional'),
    path('search_results/', views.search_results, name="search_results"),

    path('edu/update/<int:pk>/', views.edu_update, name='edu_update'),
    path('edu/create/', views.edu_create, name='edu_create'),
    path('lang/update/<int:pk>/', views.lang_update, name='lang_update'),
    path('lang/create/', views.lang_create, name='lang_create'),
    path('exp/update/<int:pk>/', views.exp_update, name='exp_update'),
    path('exp/create/', views.exp_create, name='exp_create'),

    # path('auth/login/', views.auth_log_in, name='auth_log_in'),
    path('auth/signin/', views.auth_sign_in, name='auth_sign_in'),
    path('auth/logout/', views.auth_sign_out, name='auth_sign_out'),
    # path('auth/signin/', views.auth_sign_in, name='auth_sign_in'),
    path('auth/signup/', views.auth_sign_up, name='auth_sign_up'),
    path('users/', views.users, name = 'users'),
    path('password_update/', views.password_update, name = 'password_update'),
    path('user/delete/<int:pk>', views.user_delete, name = 'user_delete'),


    path('inbox/', views.inbox, name="inbox"),
    path('inbox/read', views.inbox_read, name="inbox_read"),
    path('inbox/unread', views.inbox_unread, name="inbox_unread"),
    path('inbox/detail/<int:pk>', views.inbox_detail, name="inbox_detail"),
    path('reply/<int:pk>', views.reply, name="reply"),
    path('sent/', views.sent, name="sent"),
    path('sent/detail/<int:pk>', views.sent_detail, name="sent_detail"),
    path('drafts/', views.drafts, name="drafts"),
    path('drafts/detail/<int:pk>', views.drafts_detail, name="drafts_detail"),
    path('trash/', views.trash, name="trash"),
    path('trash/detail/<int:pk>', views.trash_detail, name="trash_detail"),
    path('compose/', views.compose, name="compose"),
]
