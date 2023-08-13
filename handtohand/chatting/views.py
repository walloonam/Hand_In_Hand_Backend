from django.http import JsonResponse
from django.shortcuts import render

from chatting.dto import *
from chatting.models import Room, Content
from post.models import Post
from user.models import User


def delete_room(request, pk):
    if request.method == 'DELETE':
        room=Room.objects.get(id=pk)
        room.delete()
        JsonResponse({"message" : "delete"})

# Create your views here.
def create_room(request):
    if request.method == 'POST':
        try:
            data = request.POST
            post_id = data.get("post_id")
            owner_id = data.get("owner_id")
            custom_id = data.get("custom_id")
            post = Post.objects.get(id=post_id)
            owner = User.objects.get(id=owner_id)
            customer = User.objects.get(id=custom_id)
            room = Room(
                post=post,
                owner=owner,
                customer=customer
            )
            room.full_clean() #데이터 유효성 검사
            room.save()
            return JsonResponse({"result": "success"})
        except Exception as e:
            print(e)
            return JsonResponse({"result": "fail"})

def show_chat(request, pk):
    if request.method == "GET":
        try:
            main=main_dto(pk)
            sub=sub_dto(pk)
            context={
                "main" : main,
                "sub" : sub
            }
        except Exception as e:
            print(e)


def create_chat(request):
    if request.method == "POST":
        try:
            data = request.POST
            content = data.get("content")
            user = data.get("user")
            room = data.get("room")
            content = Content(
                content=content,
                user=user,
                room=room
            )
            content.save()

        except Exception as e:
            print(e)
