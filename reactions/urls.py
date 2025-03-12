from django.urls import path
from reactions import views

urlpatterns = [
    path('reactions/', views.ReactionList.as_view()),
    path('reactions/<int:pk>/', views.ReactionDetail.as_view()),
]