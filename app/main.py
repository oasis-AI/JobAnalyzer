from fastapi import FastAPI

from app.routers import interview, leetcode


def get_applications():
    app = FastAPI()

    app.include_router(leetcode.router, prefix="/leetcode", tags=["leetcode"])
    app.include_router(interview.router, prefix="/interview", tags=["interview"])

    return app


app = get_applications()
