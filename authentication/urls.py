from django.urls import include, path
from .views import login, logoutFlutter, daftar, ListFeedback, DetailFeedback, get_object, AddFeedbackFlutter

urlpatterns = [
    path('', login, name='loginflutter'),
    path('logout', logoutFlutter, name='logoutflutter'),
    path('daftar', daftar, name='daftarflutter'),
    # path('json_fb', ListFeedback.as_view()),
    # path('<int:pk>/', DetailFeedback.as_view()),
    path('json', get_object, name='json'),
    path('feedback_flutter', AddFeedbackFlutter, name='feedback_flutter'),
]