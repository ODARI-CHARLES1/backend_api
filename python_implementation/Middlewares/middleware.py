from fastapi import Request, HTTPException, status
from fastapi.responses import JSONResponse
import time
from typing import Callable

async def error_handling_middleware(request: Request, call_next: Callable):
    try:
        response = await call_next(request)
        return response
    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={"detail": e.detail}
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": "Internal server error", "error": str(e)}
        )

async def logging_middleware(request: Request, call_next: Callable):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

async def rate_limit_middleware(request: Request, call_next: Callable):
    return await call_next(request)