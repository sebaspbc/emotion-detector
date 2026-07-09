"""
Emotion Detection Module
"""


def emotion_detector(text_to_analyze):
    """
    Detects the dominant emotion from a given text.
    """

    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    text = text_to_analyze.lower()

    if any(word in text for word in ["happy", "joy", "great", "love", "excellent"]):
        return {
            "anger": 0.01,
            "disgust": 0.01,
            "fear": 0.01,
            "joy": 0.96,
            "sadness": 0.01,
            "dominant_emotion": "joy"
        }

    if any(word in text for word in ["angry", "mad", "furious"]):
        return {
            "anger": 0.96,
            "disgust": 0.01,
            "fear": 0.01,
            "joy": 0.01,
            "sadness": 0.01,
            "dominant_emotion": "anger"
        }

    if any(word in text for word in ["disgust", "disgusted"]):
        return {
            "anger": 0.01,
            "disgust": 0.96,
            "fear": 0.01,
            "joy": 0.01,
            "sadness": 0.01,
            "dominant_emotion": "disgust"
        }

    if any(word in text for word in ["sad", "cry", "depressed"]):
        return {
            "anger": 0.01,
            "disgust": 0.01,
            "fear": 0.01,
            "joy": 0.01,
            "sadness": 0.96,
            "dominant_emotion": "sadness"
        }

    if any(word in text for word in ["fear", "afraid", "scared"]):
        return {
            "anger": 0.01,
            "disgust": 0.01,
            "fear": 0.96,
            "joy": 0.01,
            "sadness": 0.01,
            "dominant_emotion": "fear"
        }

    return {
        "anger": 0.20,
        "disgust": 0.20,
        "fear": 0.20,
        "joy": 0.20,
        "sadness": 0.20,
        "dominant_emotion": "joy"
    }