from django.urls import path
from .views import index, qs, jsonFlutter

urlpatterns = [
    path('', index, name='index_faq'),
    path('qs', qs, name='qs'),
    path('json', jsonFlutter, name="json"),
    

    #path('question_flutter', QuestionBox, name='question_flutter'),
]
