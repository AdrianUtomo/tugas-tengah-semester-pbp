from os import name
from django.urls import path
from .views import*


urlpatterns = [
    path('', index, name='index_infovaksin'),
    path('show_json', vaksindata, name='show_json'),
    path('infovaksin_comment', AddCommentFlutter, name='infovaksin_comment')
]