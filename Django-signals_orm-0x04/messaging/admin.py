from django.contrib import admin
from .models import Message, Notification, MessageHistory

class MessageHistoryInline(admin.TabularInline):
    model = MessageHistory
    extra = 0
    readonly_fields = ['old_content', 'edited_at', 'edited_by']

class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'sender', 'receiver', 'edited', 'timestamp']
    inlines = [MessageHistoryInline]

admin.site.register(Message, MessageAdmin)
admin.site.register(Notification)
admin.site.register(MessageHistory)

