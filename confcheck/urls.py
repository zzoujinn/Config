from django.urls import path
from confcheck import views

app_name = 'confcheck'

urlpatterns = [
    path('', views.index, name='index'),
    path('quick_query/', views.quick_query, name='key_vaules_to_project'),
    path('key_to_values_project/', views.key_to_values_project, name='key_to_values_project'),
    path('values_to_key_project/', views.values_to_key_project, name='values_to_key_project'),
    path('config_check/', views.config_check, name='config_check'),

    # path('quick_query/', views.quick_query, name='quick_query'),
]