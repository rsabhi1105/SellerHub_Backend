from rest_framework import serializers

from testing_app.models import Singer, Song, Sales_product


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["song_name", "singer"]


class SingerSerializer(serializers.ModelSerializer):
    song = SongSerializer(many=True)

    class Meta:
        model = Singer
        fields = ["name", "song"]


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales_product
        fields = ["user", "product_order", "quantity",
                  "created_at", "updated_at"]
