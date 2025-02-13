from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
import time

class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request.state.something = "something"
        start_time = time.time()
        print(f"Incoming request: {request.method} {request.url}")
        response: Response = await call_next(request)
        
        process_time = time.time() - start_time
        
        print(f"Completed in {process_time:.2f}s with status code {response.status_code}")
        
        return response