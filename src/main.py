import uvicorn
from starlette.applications import Starlette

from admin import admin

app = Starlette()
admin.mount_to(app)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        port=5000,
        reload=False,
    )
