import logging
from datetime import time, datetime, timedelta
from django.http import HttpResponseForbidden
from collections import defaultdict
from django.http import HttpResponseForbidden


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Configure logger
        self.logger = logging.getLogger('django.request_logger')
        handler = logging.FileHandler('requests.log')
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else 'Anonymous'
        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}"
        self.logger.info(log_message)

        response = self.get_response(request)
        return response


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

class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.request_log = defaultdict(list)  # { ip: [timestamp1, timestamp2, ...] }
        self.limit = 5  # messages
        self.time_window = timedelta(minutes=1)

    def __call__(self, request):
        if request.method == 'POST':
            ip = self.get_ip_address(request)
            now = datetime.now()

            # Remove timestamps outside the time window
            self.request_log[ip] = [
                timestamp for timestamp in self.request_log[ip]
                if now - timestamp < self.time_window
            ]

            if len(self.request_log[ip]) >= self.limit:
                return HttpResponseForbidden("Rate limit exceeded: max 5 messages per minute.")

            self.request_log[ip].append(now)

        return self.get_response(request)

    def get_ip_address(self, request):
        # Support X-Forwarded-For if behind proxy/load balancer
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


class RolepermissionMiddleware
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user

        # Ensure user is authenticated
        if user.is_authenticated:
            # Check role-based permissions
            user_role = getattr(user, 'role', None)  # Assume a 'role' attribute exists on the user model
            if user_role not in ['admin', 'moderator']:
                return HttpResponseForbidden("Access denied: insufficient permissions.")
        else:
            return HttpResponseForbidden("Access denied: user not authenticated.")

        return self.get_response(request)
