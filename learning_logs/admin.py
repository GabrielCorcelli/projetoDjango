from django.contrib import admin
from learning_logs.models import Topic,Entry



admin.site.register(Topic)
@admin.register(Entry)
class TopicAdmin(admin.ModelAdmin):
    list_display = ["text","topic"]

# Register your models here.
