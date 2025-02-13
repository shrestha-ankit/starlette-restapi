from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.middleware import Middleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.cors import CORSMiddleware
from app.middlewares.middleware import CustomMiddleware
from app.routes.user_route import user_routes
from app.routes.home import home_page


middleware = [
    Middleware(
        TrustedHostMiddleware,
        allowed_hosts=["localhost", "*.example.com"]
    ),
    Middleware(CORSMiddleware, allow_origins=["*"])
]


app = Starlette(debug=True, routes=[
    Route("/", home_page), 
    Mount("/users", routes=user_routes)], middleware=middleware)

