from fastapi import APIRouter
from datetime import datetime

router = APIRouter()


@router.post("/create")
async def create_user():
    return "user created"


@router.post("/login")
async def login():
    return "Login success"


@router.post("/location/update")
async def location_update():
    return "Event Logged"
