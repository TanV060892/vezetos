from fastapi import APIRouter
from api.endpoints import webhook,data,tasks,sync
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
async def default_route():
    return JSONResponse(status_code=200, content={"status": True,"data":{"message": "Welcome to Vezetos Platform"}})

router.include_router(webhook.router, prefix="")
router.include_router(data.router, prefix="")
router.include_router(tasks.router, prefix="")
router.include_router(sync.router, prefix="")

@router.route("/{full_path:path}")
async def catch_all(full_path: str):
    return JSONResponse(status_code=404, content={"status": False, "errors": [{"message": "Please provide a valid URL"}]})