from django.core import serializers

from chatting.models import Content, Room
from user.models import User


# def main_dto(pk):
#     user=User.object.get(pk=pk)
#     main_room = Room.object.filter(owner=user)
#     for m in main_room:
#
#
#
# def sub_dto(pk):
