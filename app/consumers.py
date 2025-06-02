import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    group_name = "notifications_group"

    async def connect(self):
        print(f"WebSocket connected: {self.channel_name}")

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()
        
        await self.send(text_data=json.dumps({
            "type": "connection_established",
            "message": "You are now connected to the notifications"
        }))
        
    async def disconnect(self, close_code):
        print(f"WebSocket disconnected: {self.channel_name} with code {close_code}")
        
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get("message")

        print(f"Received message from {self.channel_name}: {message}")


    async def send_notification(self, event):
        message_data = event["message"]

        print(f"Sending notification to {self.channel_name}: {message_data}")

        await self.send(text_data=json.dumps({
            "type": 'notification',
            "message": message_data
        }))