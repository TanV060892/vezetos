from fastapi import FastAPI,Request
from utils.db import create_db_and_tables
from utils.routes import router as api_router
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException  

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()

# Include the router from the routes file
app.include_router(api_router)


# Custom exception handler for RequestValidationError (validation errors)
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    error_messages = []
    for error in exc.errors():
        field = error["loc"][-1]
        msg = f"{field} is required"
        error_messages.append({"message": msg,"code":'VZ422'})   
    return JSONResponse(status_code=422, content={"status": False, "errors": error_messages})

@app.exception_handler(StarletteHTTPException)
async def authentication_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(status_code=exc.status_code, content={"status": False, "errors": [{"message":"Please provide valid authorization token","code":'VZ401',"reason": exc.detail}]})

