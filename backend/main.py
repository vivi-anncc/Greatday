from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from database import engine, get_db
from models import Activity, ActivityHistory, DailySurvey, User

from schemas import (
    ActivityCreate,
    ActivityHistoryCreate,
    DailySurveyCreate,
    UserCreate
)




app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Event App API is running!"
    }


@app.get("/db-test")
def database_test():

    with engine.connect() as connection:
        result = connection.execute(text("SELECT NOW()"))

        database_time = result.scalar()

    return {
        "message": "PostgreSQL connection works!",
        "database_time": database_time
    }


@app.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        username=user.username
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()

    return users

@app.post("/activities")
def create_activity(
    activity: ActivityCreate,
    db: Session = Depends(get_db)
):
    new_activity = Activity(
        name=activity.name,
        description=activity.description
    )

    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)

    return new_activity


@app.post("/activity-history")
def create_activity_history(
    history: ActivityHistoryCreate,
    db: Session = Depends(get_db)
):
    new_history = ActivityHistory(
        user_id=history.user_id,
        activity_id=history.activity_id,
        date=history.date
    )

    db.add(new_history)
    db.commit()
    db.refresh(new_history)

    return new_history

@app.post("/daily-surveys")
def create_daily_survey(
    survey: DailySurveyCreate,
    db: Session = Depends(get_db)
):
    new_survey = DailySurvey(
        user_id=survey.user_id,
        date=survey.date,
        mood=survey.mood,
        energy=survey.energy,
        available_minutes=survey.available_minutes
    )

    db.add(new_survey)
    db.commit()
    db.refresh(new_survey)

    return new_survey

@app.get("/users/{user_id}/activity-history")
def get_activity_history(
    user_id: int,
    db: Session = Depends(get_db)
):
    history = (
        db.query(ActivityHistory)
        .filter(ActivityHistory.user_id == user_id)
        .all()
    )

    return history

@app.get("/users/{user_id}/daily-surveys")
def get_daily_surveys(
    user_id: int,
    db: Session = Depends(get_db)
):
    surveys = (
        db.query(DailySurvey)
        .filter(DailySurvey.user_id == user_id)
        .all()
    )

    return surveys




    


