from django.shortcuts import render, get_object_or_404
from messaging.models import Message
from django.contrib.auth.decorators import login_required
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
    # Fetch the parent message with sender and receiver in one query
    message = get_object_or_404(
        Message.objects.select_related('sender', 'receiver').prefetch_related('replies__sender', 'replies__receiver'),
        id=message_id,
        parent_message__isnull=True
    )

    # Recursively fetch replies
    def get_thread(msg):
        return {
            'message': msg,
            'replies': [get_thread(reply) for reply in msg.replies.all()]
        }

    thread = get_thread(message)


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
