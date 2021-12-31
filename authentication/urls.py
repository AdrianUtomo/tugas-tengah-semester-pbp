from django.urls import include, path
from .views import login, logoutFlutter, daftar, ListFeedback, DetailFeedback

urlpatterns = [
    path('', login, name='loginflutter'),
    path('logout', logoutFlutter, name='logoutflutter'),
    path('daftar', daftar, name='daftarflutter'),

    path('json_fb', ListFeedback.as_view()),
    path('<int:pk>/', DetailFeedback.as_view())
]