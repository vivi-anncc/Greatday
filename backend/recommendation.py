from models import Activity, ActivityHistory
from database import SessionLocal


def get_recent_activity_ids(
    user_id: int,
    db
) -> set[int]:
    history = (
        db.query(ActivityHistory)
        .filter(ActivityHistory.user_id == user_id)
        .all()
    )

    return {
        record.activity_id
        for record in history
    }


def recommend_activity(
    mood: int,
    energy: int,
    available_minutes: int,
    activities: list[Activity],
    recent_activity_ids: set[int]
):
    suitable_activities = [
        activity
        for activity in activities
        if (
            activity.energy_required <= energy
            and activity.minimum_minutes <= available_minutes
        )
    ]

    if not suitable_activities:
        return None

    best_activity = None
    best_score = -1

    for activity in suitable_activities:
        score = 0

 
        energy_difference = abs(
            energy - activity.energy_required
        )

        score += 10 - energy_difference

 
        extra_time = (
            available_minutes - activity.minimum_minutes
        )

        if extra_time <= 30:
            score += 5

 
        if activity.id in recent_activity_ids:
            score -= 5
 
        if score > best_score:
            best_score = score
            best_activity = activity

    return best_activity


if __name__ == "__main__":
    db = SessionLocal()

 
    user_id = 1

 
    activities = db.query(Activity).all()

 
    recent_activity_ids = get_recent_activity_ids(
        user_id,
        db
    )

 
    recommendation = recommend_activity(
        mood=8,
        energy=6,
        available_minutes=90,
        activities=activities,
        recent_activity_ids=recent_activity_ids
    )

    if recommendation:
        print(
            f"Recommendation: {recommendation.name}"
        )
    else:
        print("No suitable activity found.")

    db.close()
