from collections import Counter


def generate_weekly_report(moods):

    if not moods:
        return {
            "summary": "No mood data available."
        }

    mood_counts = Counter([m.mood for m in moods])

    most_common = mood_counts.most_common(1)[0][0]

    return {
        "dominant_mood": most_common,
        "total_entries": len(moods),
        "mood_breakdown": dict(mood_counts)
    }
