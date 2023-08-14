from django.urls import path

from chatting import views

urlpatterns = [
    path("create/room/", views.create_room, name="create_chat"),
    path("", views.show_chat, name="show_chat"),
    path("delete/<int:pk>/", views.delete_room, name="delete_room"),
    path("choice/",views.choice,name="choice_chat")
]