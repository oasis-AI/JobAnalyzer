from fastapi import APIRouter

router = APIRouter(tags=["login"])


@router.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0

    return division_by_zero
