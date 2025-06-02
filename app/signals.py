from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
from .models import Post, Comment

@receiver(post_save, sender=Post)
def post_created_notification(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        group_name = "notifications_group"

        message_data = {
            "type": "post_created",
            "post_id": instance.id,
            "title": instance.title,
            "author": instance.author.username,
        }

        print(f"Sending notification for new post: {instance.title}")

        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                "type": "send.notification",
                "message": message_data
            }
        )

@receiver(post_save, sender=Comment)
def comment_created_notification(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        group_name = "notifications_group"

        message_data = {
            "type": "comment_created",
            "comment_id": instance.id,
            "post_id": instance.post.id,
            "post_title": instance.post.title,
            "author": instance.author.username,
            "text": instance.text[:50] + "..." if len(instance.text) > 50 else instance.text,
        }

        print(f"Sending notification for new comment by {instance.author.username} on post {instance.post.title}")

        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                "type": "send.notification",
                "message": message_data
            }
        )
        