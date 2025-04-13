import time
from asyncio import sleep
from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.core.db import engine
from app.models.user import Address, User

router = APIRouter(tags=["login"])


@router.get("/user/create")
async def trigger_error():
    with Session(engine) as session:
        spongebob = User(
            name="spongebob",
            fullname="Spongebob Squarepants",
            addresses=[Address(email_address="spongebob@sqlalchemy.org")],
        )
        sandy = User(
            name="sandy",
            fullname="Sandy Cheeks",
            addresses=[
                Address(email_address="sandy@sqlalchemy.org"),
                Address(email_address="sandy@squirrelpower.org"),
            ],
        )
        patrick = User(name="patrick", fullname="Patrick Star")
        session.add_all([spongebob, sandy, patrick])
        session.commit()


@router.get("/user/sleep")
async def trigger_error1():
    await sleep(60)


@router.get("/user/async_time_sleep")
async def trigger_error2():
    time.sleep(60)


@router.get("/user/time_sleep")
def trigger_error3():
    time.sleep(60)


@router.get("/user/seecss")
def trigger_error4():
    print("执行成功")

