from django.http import JsonResponse
from django.shortcuts import render

from chatting.dto import *
from chatting.models import Room, Content
from post.models import Post
from user.models import User, Token

from chatting.dto import main_dto, sub_dto


def delete_room(request, pk):
    if request.method == 'DELETE':
        room=Room.objects.get(id=pk)
        room.delete()
        JsonResponse({"message": "delete"})

# Create your views here.
def create_room(request):
    if request.method == 'POST':
        try:
            data = request.POST
            post_id = data.get("post_id")
            post = Post.objects.get(id=post_id)
            owner = post.user
            token = data.get("token")
            token = Token.objects.get(token=token)
            customer = User.objects.get(email=token.email)
            customer = customer.nickname
            room = Room(
                post=post.title,
                owner=owner,
                customer=customer
            )
            room.full_clean() #데이터 유효성 검사
            room.save()
            return JsonResponse({"result": "success"})
        except Exception as e:
            print(e)
            return JsonResponse({"result": "fail"})

def show_chat(request):
    if request.method == "POST":
        user_token=request.POST.get("token")
        user = Token.objects.get(token=user_token)
        user_id=user.pk
        try:
            main=main_dto(user_id)
            sub=sub_dto(user_id)
            context={
                "main": main,
                "sub": sub
            }
            return JsonResponse(context)
        except Exception as e:
            print(e)


def create_chat(request):
    if request.method == "POST":
        try:
            data = request.POST
            content = data.get("content")
            user = data.get("token")
            user = Token.objects.get(email=user.email)
            user = user.nickname
            room = data.get("room")
            content = Content(
                content=content,
                user=user,
                room=room
            )
            content.save()

        except Exception as e:
            print(e)

def choice(request):
    if request.method=="POST":
        try:
            room_id= request.POST.get("room_id")
            room = Room.objects.get(id=room_id)
            user1 = User.objects.get(id=room.owner)
            user2 = User.objects.get(id=room.customer)
            post = Post.objects.get(id=room.post)
            user1.point -= post.point
            user2.point += post.point
            user1.save()
            user2.save()
        except Exception as e:
            print(e)