from fastapi import APIRouter, FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND

router = APIRouter(tags=["fast api demo"])


# curl "http://localhost:8081/healthz"
@router.get("/healthz")
async def healthz_handler():
    return {"message": "ok"}


app = FastAPI(title="users managerment demo")
app.include_router(router)


# curl "http://localhost:8081/"
@app.get("/")
async def home_handler():
    return {"message": "welcome to fast api"}


# curl "http://localhost:8081/not_found"
@app.exception_handler(HTTP_404_NOT_FOUND)
async def not_found_hanlder(request: Request, err: HTTPException):
    _ = err
    return JSONResponse(
        status_code=HTTP_404_NOT_FOUND,
        content={
            "message": "the resource you are looking for is not found",
            "path": request.url.path,
        },
    )


def main():
    import uvicorn

    port = 8081
    print(f"start fast api server at: {port}")
    uvicorn.run(app, host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
