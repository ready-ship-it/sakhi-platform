def get_coping_suggestion(mood):

    suggestions = {
        "sad": "Try reaching out to a friend or writing your thoughts in a journal.",
        "anxious": "Take 5 deep breaths and focus on what you can control right now.",
        "stressed": "Take a short walk and give yourself permission to rest.",
        "lonely": "Connect with someone you trust, even with a simple message.",
        "happy": "Celebrate what's going well and record it in your journal."
    }

    return suggestions.get(
        mood.lower(),
        "Take a few moments for self-care today."
    )
