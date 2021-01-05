from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='main_page'),
    path('forum', views.forum, name='forum_page'),
    path('create_task', views.create_task, name='create_task'),
    path('calculator', views.calculator_def, name='Calculator'),
    path('submit_query', views.submit_query, name='submit_query'),
    path('fighting_page', views.fighting_page, name='fight'),
    path('fighting_create', views.fighting_page_form, name='fight_create'),
    path('users', views.user_stattts, name='someuser')
]
