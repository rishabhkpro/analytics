from fastapi import APIRouter, Request, Depends, Query
from sqlalchemy.orm import Session
from datetime import datetime
from model import Event
from dtos import (
    UserCreateDto,
    UserLoginDto,
    LocationUpdateDto,
    EventDataDto,
    EventsDataDto,
)
from database import get_db

router = APIRouter()


@router.post("/create", status_code=201)
async def create_user(
    request_body: UserCreateDto,
    request: Request,
    db: Session = Depends(get_db),
):

    # delete password before storing request body
    del request_body.user_password

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


@router.post("/login", status_code=200)
async def login(
    request_body: UserLoginDto,
    request: Request,
    db: Session = Depends(get_db),
):

    # delete password before storing request body
    del request_body.user_password

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


@router.post("/location/update", status_code=200)
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


@router.get("/events", status_code=200, response_model=EventsDataDto)
async def get_events(
    event_date: str = Query("", description="Date format is yyyy-mm-dd"),
    user_name: str = Query("", description="Retreaving basing on user name status"),
    api_status: str = Query("", description="Retreaving basing on api status"),
    db: Session = Depends(get_db),
):
    events_data = db.query(Event).all()
    events_dto = []
    for event in events_data:
        temp = EventDataDto(
            user_name=event.user_name,
            api_method=event.api_method,
            api_url=event.api_url,
            api_body=event.api_body,
            lat=event.lat,
            long=event.long,
            api_status=event.api_status,
            created_at=event.created_at.strftime("%d-%m-%Y %H:%M:%S"),
        )
        events_dto.append(temp)

    return EventsDataDto(body=events_dto, msg="success")
