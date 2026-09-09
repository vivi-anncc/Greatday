def recommend_activity(mood: int, energy: int, available_minutes: int):
    if energy >= 7 and available_minutes >= 90:
        return "Hiking"

    if energy >= 6 and available_minutes >= 30:
        return "Go for a walk"

    if mood <= 3:
        return "Reading"

    return "Try something relaxing"

if __name__ == "__main__":
    result = recommend_activity(
        mood=5,
        energy=8,
        available_minutes=60
    )

    print(result)
