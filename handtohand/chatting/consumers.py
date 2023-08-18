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
        # await self.channel_layer.group_add(self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
        except json.JSONDecodeError as e:
            print("JSON decoding error:", e)
            return
        content = text_data_json.get('content')
        room_id = text_data_json.get('room_id')
        user_id = text_data_json.get('user_id')
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
    async def chat_message(self, event):
        print(event)
        content = event.get('content')
        user_id = event.get('user_id')
        room_id = event.get('room_id')

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'content': content,
            "user_id" : user_id,
            "room_id" : room_id,
        }))