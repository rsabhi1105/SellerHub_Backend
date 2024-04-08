from rest_framework import serializers

from chat_bot.models import ChatBot


class ChatBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatBot
        fields = [
            "user", "user_chat", "response_chat",
            "created_at", "updated_at"
        ]
