from django.shortcuts import render, get_object_or_404
from messaging.models import Message
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User

@login_required
def delete_user(request):
    user = request.user
    logout(request)
    user.delete()
    return redirect('login')  # Update to your login route name


@login_required
def message_thread_view(request, message_id):
    # Get root message
    root_message = get_object_or_404(
        Message.objects.select_related('sender', 'receiver'),
        id=message_id,
        parent_message__isnull=True
    )

    # Recursive function using Message.objects.filter
    def fetch_replies(message):
        replies = Message.objects.filter(parent_message=message).select_related('sender', 'receiver')
        return [
            {
                'message': reply,
                'replies': fetch_replies(reply)
            }
            for reply in replies
        ]

    thread = {
        'message': root_message,
        'replies': fetch_replies(root_message)
    }


@login_required
def send_message(request):
    if request.method == "POST":
        receiver_id = request.POST.get('receiver')
        content = request.POST.get('content')
        parent_id = request.POST.get('parent_message')

        receiver = get_object_or_404(User, id=receiver_id)
        parent_message = None
        if parent_id:
            parent_message = get_object_or_404(Message, id=parent_id)

        Message.objects.create(
            sender=request.user,
            receiver=receiver,
            content=content,
            parent_message=parent_message
        )


@login_required
def unread_messages_view(request):
    # Uses custom manager and .only() to retrieve specific fields
    unread_messages = Message.unread.unread_for_user(request.user)  # Message.unread.unread_for_user
    unread_messages = unread_messages.only('id', 'sender', 'content', 'timestamp')  # .only
    return render(request, 'messaging/unread_inbox.html', {'messages': unread_messages})


@cache_page(60)  # Cache for 60 seconds
@login_required
def conversation_view(request, user_id):
    messages = Message.objects.filter(
        sender=request.user, receiver__id=user_id
    ) | Message.objects.filter(
        sender__id=user_id, receiver=request.user
    )
    messages = messages.order_by('timestamp')
    return render(request, 'messaging/conversation.html', {'messages': messages})
