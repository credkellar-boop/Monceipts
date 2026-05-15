from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
import time

class RateLimitMiddleware(BaseHTTPMiddleware):
    # Limit to 10 receipt generations per minute per IP
    def __init__(self, app, limit: int = 10, window: int = 60):
        super().__init__(app)
        self.limit = limit
        self.window = window
        self.clients = {}

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        now = time.time()
        
        # Clean up old entries
        self.clients = {ip: times for ip, times in self.clients.items() if now - times[-1] < self.window}
        
        if client_ip not in self.clients:
            self.clients[client_ip] = []
        
        if len(self.clients[client_ip]) >= self.limit:
            raise HTTPException(status_code=429, detail="Too many receipt requests.")
        
        self.clients[client_ip].append(now)
        return await call_next(request)
