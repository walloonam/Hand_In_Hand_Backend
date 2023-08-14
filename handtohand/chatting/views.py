import json

from django.core import serializers
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

from chatting.dto import *
from chatting.models import Room, Content
from post.models import Post
from user.models import User, Token

from user.models import Attendance


# from chatting.dto import main_dto, sub_dto


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
            customer = User.objects.get(id=token.email_id)
            customer = customer
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


def main_dto(pk):
    nested_json = {"main": []}
    user = User.objects.get(pk=pk)
    main_room = Room.objects.filter(owner=user)

    for m in main_room:
        chat = Content.objects.filter(Q(user=user) | Q(user=m.customer))
        chat_data = []
        for c in chat.order_by('pk'):  # Order chat by pk
            chat_data.append({
                "pk": c.pk,
                "fields": {
                    "content": c.content,
                    "user": c.user.nickname,
                    "room": c.room.id
                }
            })
        main_content = {
            "owner" : m.owner.adopt_count,
            "custom" : m.customer.adopt_count,
            "room_id": m.pk,
            "title": m.post.title,
            "chat": chat_data
        }
        nested_json["main"].append(main_content)

    return nested_json


def sub_dto(pk):
    nested_json = {"sub": []}
    user = User.objects.get(pk=pk)
    sub_room = Room.objects.filter(customer=user)

    for m in sub_room:
        chat = Content.objects.filter(Q(user=user) | Q(user=m.owner))
        chat_data = []
        for c in chat.order_by('pk'):  # Order chat by pk
            chat_data.append({
                "pk": c.pk,
                "fields": {
                    "content": c.content,
                    "user": c.user.nickname,
                    "room": c.room.id
                }
            })
        sub_content = {
            "owner": m.owner.adopt_count,
            "custom": m.customer.adopt_count,
            "room_id": m.pk,
            "title": m.post.title,
            "chat": chat_data
        }
        nested_json["sub"].append(sub_content)

    return nested_json


def show_chat(request):
    if request.method == "POST":
        user_token = request.POST.get("token")
        user = Token.objects.get(token=user_token)
        user_id = user.email_id
        user=User.objects.get(id=user_id)
        print(user_id)
        try:
            main = main_dto(user_id)
            sub = sub_dto(user_id)
            context = {
                "user": user.nickname,
                "main": main,
                "sub": sub
            }
            return JsonResponse(context)
        except Exception as e:
            print(e)
            return JsonResponse({"error": str(e)}, status=500)


def create_chat(request):
    if request.method == "POST":
        try:
            data = request.POST
            content = data.get("content")
            user_token = data.get("token")
            token = Token.objects.get(token=user_token)
            user= User.objects.get(id=token.email_id)
            user_nickname = user.nickname
            room = data.get("room_id")
            room=Room.objects.get(id=room)

            content_obj = Content(
                content=content,
                user=user,
                room=room
            )
            content_obj.save()

            return JsonResponse({"message": "success"})
        except Exception as e:
            print(e)
            return JsonResponse({"message": "error", "error_details": str(e)})
    else:
        return JsonResponse({"message": "Invalid request method"})


def choice(request):
    if request.method == "POST":
        try:
            room_id = request.POST.get("room_id")
            room = Room.objects.get(id=room_id)
            user1 = User.objects.get(id=room.owner_id)
            user2 = User.objects.get(id=room.customer_id)
            post = Post.objects.get(id=room.post_id)

            user1.point -= post.point
            user2.point += post.point
            user1.save()
            user2.save()

            # 뷰 함수가 성공적으로 처리되었음을 응답으로 알려주기 위해 JsonResponse를 반환
            return JsonResponse({"message": "success"})

        except Exception as e:
            print(e)
            # 예외가 발생하면 에러 메시지와 함께 500 상태 코드로 응답
            return JsonResponse({"error": str(e)}, status=500)




