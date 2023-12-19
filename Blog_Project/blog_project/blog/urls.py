from django.urls import path
from blog import views

urlpatterns = [
    path('', views.post_list_view),
    path('tag/<slug:tag_slug>/', views.post_list_view, name='post_list_by_tag_name'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail_view, name='post_detail'),
    path('<int:id>/share/', views.mail_send_view),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about_us_view),
    path('home/', views.home_view),
]