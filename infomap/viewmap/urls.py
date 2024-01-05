from viewmap import views
from django.urls import path

app_name = 'pybo'

urlpatterns = [
    path('',views.test, name='test'),
    path('question/<int:question_id>/',views.detail,name = 'detail'),
    path('answer/create/<int:question_id>/',views.answer_create, name='answer_create'),
]
