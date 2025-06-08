# Django-Middleware-0x03/chats/middleware.py
from datetime import datetime, time
from django.http import HttpResponseForbidden

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Define allowed access time range: 6AM to 9PM
        self.start_time = time(6, 0)   # 6:00 AM
        self.end_time = time(21, 0)    # 9:00 PM

    def __call__(self, request):
        current_time = datetime.now().time()

        # Check if current time is outside allowed range
        if not (self.start_time <= current_time <= self.end_time):
            return HttpResponseForbidden("Access to the messaging app is forbidden outside 6AM-9PM.")

        response = self.get_response(request)
        return response
