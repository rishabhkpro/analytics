from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Float


class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, auto_increment=True, index=True)
    user_name = Column(String, nullable=True, default="")
    api_method = Column(String, nullable=True)
    api_url = Column(String, nullable=True)
    api_body = Column(String, nullable=True)
    api_status = Column(String, nullable=True)
    lat = Column(Float, nullable=True)
    long = Column(Float, nullable=True)
    created_at = Column(DateTime, nullable=True)
