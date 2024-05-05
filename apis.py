from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from model import Event
from dtos import UserCreateDto, UserLoginDto, LocationUpdateDto
from database import get_db

router = APIRouter()


@router.post("/create")
async def create_user(
    request_body: UserCreateDto,
    request: Request,
    db: Session = Depends(get_db),
):

    even_data = Event(user_name=request_body.user_name)
    even_data.api_url = request.url.path
    even_data.api_method = request.method
    even_data.api_body = str(request_body)
    even_data.api_status = "success"
    if request_body.lat:
        even_data.lat = request_body.lat
    if request_body.long:
        even_data.long = request_body.long
    even_data.created_at = datetime.now()

    db.add(even_data)
    db.flush()
    db.commit()

    return "user created"


@router.post("/login")
async def login(
    request_body: UserLoginDto,
    request: Request,
    db: Session = Depends(get_db),
):
    even_data = Event(user_name=request_body.user_name)
    even_data.api_url = request.url.path
    even_data.api_method = request.method
    even_data.api_body = str(request_body)
    even_data.api_status = "success"
    if request_body.lat:
        even_data.lat = request_body.lat
    if request_body.long:
        even_data.long = request_body.long
    even_data.created_at = datetime.now()

    db.add(even_data)
    db.flush()
    db.commit()
    return "Login success"


@router.post("/location/update")
async def location_update(
    request_body: LocationUpdateDto,
    request: Request,
    db: Session = Depends(get_db),
):
    even_data = Event(user_name=request_body.user_name)
    even_data.api_url = request.url.path
    even_data.api_method = request.method
    even_data.api_body = str(request_body)
    even_data.api_status = "success"
    even_data.lat = request_body.lat
    even_data.long = request_body.long
    even_data.created_at = datetime.now()

    db.add(even_data)
    db.flush()
    db.commit()
    return "Event Logged"
