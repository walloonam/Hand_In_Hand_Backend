import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        #이친구둘은 없어도 될지도
        # self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        # self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        content = text_data_json['content']
        room_id = text_data_json['room_id']
        user_id = text_data_json['user_id']
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                "content":content,
                "room_id" : room_id,
                "user_id" : user_id,
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        print(event)
        content = event['content']
        user_id = event['user_id']
        room_id = event['room_id']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'content': content,
            "user_id" : user_id,
            "room_id" : room_id,
        }))