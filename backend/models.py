from datetime import date

from sqlalchemy import Date, ForeignKey, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )


class Activity(Base):
    __tablename__ = "activities"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    energy_required: Mapped[int] = mapped_column(
        nullable=False
    )

    minimum_minutes: Mapped[int] = mapped_column(
        nullable=False
    )



class ActivityHistory(Base):
    __tablename__ = "activity_history"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    activity_id: Mapped[int] = mapped_column(
        ForeignKey("activities.id"),
        nullable=False
    )

    date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

class DailySurvey(Base):
    __tablename__ = "daily_surveys"

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "date",
            name="unique_user_survey_date"
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    mood: Mapped[int] = mapped_column(nullable=False)

    energy: Mapped[int] = mapped_column(nullable=False)

    available_minutes: Mapped[int] = mapped_column(nullable=False)



