from django.core import serializers

from chatting.models import Content, Room
from django.db.models import Q
from user.models import User


# def main_dto(pk):
#     nested_json={"main":[]}
#     user=User.object.get(pk=pk)
#     main_room = Room.object.filter(owner=user.nickname)
#     for m in main_room:
#         chat = Content.objects.filter(Q(user=user.nickname)|Q(user=m.customer))
#         chats= serializers.serialize("json", chat)
#         main_content = {
#             "title" : m.post,
#             "chat" : chats
#         }
#         nested_json["main"].append(main_content)
#     json_data = serializers.serialize("json", nested_json)
#
#     return json_data
#
#
# def sub_dto(pk):
#     nested_json = {"sub": []}
#     user = User.object.get(pk=pk)
#     main_room = Room.object.filter(customer=user.nickname)
#     for m in main_room:
#         chat = Content.objects.filter(Q(user=user.nickname) | Q(user=m.owner))
#         chats = serializers.serialize("json", chat)
#         main_content = {
#             "title": m.post,
#             "chat": chats
#         }
#         nested_json["main"].append(main_content)
#     json_data = serializers.serialize("json", nested_json)
#     return json_data
# #
# #
# # def sub_dto(pk):
# # main:{
