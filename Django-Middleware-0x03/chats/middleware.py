from datetime import datetime, timedelta
from django.http import HttpResponseForbidden
from collections import defaultdict

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
