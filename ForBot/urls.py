from django.contrib import admin
from django.urls import path
from question.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AnswerListView.as_view(),)
]
