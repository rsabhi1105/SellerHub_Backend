from django.contrib import admin

from testing_app.models import Singer, Song, Sales_product


# Register your models here.
@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ["song_name", "singer"]


@admin.register(Sales_product)
class SalesAdmin(admin.ModelAdmin):
    list_display = ["user", "product_order", "quantity",
                    "created_at", "updated_at"]
