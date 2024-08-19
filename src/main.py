import uvicorn
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.routing import Route

from admin import admin


async def home_root(request: Request):
    return RedirectResponse(url="/program-pg-view/list")


routes = [Route("/", endpoint=home_root)]

app = Starlette(routes=routes)
admin.mount_to(app)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        port=5000,
        reload=False,
    )
