from datetime import date

from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str


class ActivityCreate(BaseModel):
    name: str
    description: str | None = None


class ActivityHistoryCreate(BaseModel):
    user_id: int
    activity_id: int
    date: date
    
class DailySurveyCreate(BaseModel):
    user_id: int
    date: date
    mood: int
    energy: int
    available_minutes: int

