from starlette.responses import JSONResponse
from starlette.requests import Request
from starlette.routing import Route
from app.services.user_service import get_all_users_handler, create_user_handler, get_user_handler, update_user_handler, delete_user_handler
from starlette.middleware import Middleware
from app.middlewares.middleware import CustomMiddleware

async def list_users(_: Request) -> JSONResponse:
    
    users = get_all_users_handler()
    return JSONResponse(status_code=201, content={"message": "Successfully fetched user", "users": users}) 


async def get_user_by_id(req: Request) -> JSONResponse:
    user_id = int(req.path_params.get("user_id"))
    if not user_id:
        return JSONResponse({"message": "User Id required"})
    
    user = get_user_handler(user_id)
    
    if not user: 
        return JSONResponse({"message": "User not found"}, status_code=404)
    
    return JSONResponse({"message": "User Found", "user": user}, status_code=201)


async def create_user(req: Request) -> JSONResponse:
    print(f"data from middleware: {req.state.something}")
    data = await req.json()
    name = data.get("name")
    email = data.get("email")
    
    if not name or not email:
        return JSONResponse({"message": "name and email required"})
    
    new_user = create_user_handler(name, email)
    
    if new_user:
        return JSONResponse({"message": "Successfully created new user", "new_user": new_user}, status_code=201)
    
    return JSONResponse({"message": "Failed to create new user"})


async def update_user(req: Request) -> JSONResponse:
    user_id = int(req.query_params.get("user_id"))
    update_data = await req.json()
    
    update_user = update_user_handler(user_id, update_data)
    
    if not update_user:
        return JSONResponse({"message": "Error updating user(user not found!)"}, status_code=404)
    
    return JSONResponse({"message": "Successfully updated user", "user": update_user})


async def delete_user(req: Request) -> JSONResponse:
    user_id = int(req.path_params.get("user_id"))
    
    if not user_id:
        return JSONResponse({"message": "user id required"}, status_code=404)
    
    deleted_user = delete_user_handler(user_id)
    
    if not delete_user: 
        return JSONResponse({"message": "User not found"})
    
    return JSONResponse({ "message": "Successfully deleted user", "deleted_user": deleted_user })


middlewares = [
     Middleware(CustomMiddleware)
]

user_routes = [
    Route("/", list_users, methods=["GET"]),
    Route("/{user_id}", get_user_by_id, methods=["GET"]),
    Route("/create", create_user, methods=["POST"], middleware=middlewares),
    Route("/update", update_user, methods=["PATCH"]),
    Route("/delete/{user_id}", delete_user, methods=["DELETE"])
]

