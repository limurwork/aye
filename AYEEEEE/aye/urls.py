from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='home'),
    path('input', views.input, name='input'),
    path('post/<int:post_id>/', views.name_user.as_view(), name='post')

   # path('<int:pt/update>', views.update, name='input_update'),

]