from starlette.responses import JSONResponse

async def home_page(request):
    return JSONResponse({"success":True, "message": "Home page"})