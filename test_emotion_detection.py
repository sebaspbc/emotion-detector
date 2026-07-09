import unittest

from EmotionDetection import emotion_detector


class EmotionDetectionTests(unittest.TestCase):

    def test_joy(self):
        self.assertEqual(
            emotion_detector("I am happy today")["dominant_emotion"],
            "joy"
        )

    def test_anger(self):
        self.assertEqual(
            emotion_detector("I am angry")["dominant_emotion"],
            "anger"
        )

    def test_disgust(self):
        self.assertEqual(
            emotion_detector("I am disgusted")["dominant_emotion"],
            "disgust"
        )

    def test_sadness(self):
        self.assertEqual(
            emotion_detector("I am sad")["dominant_emotion"],
            "sadness"
        )

    def test_fear(self):
        self.assertEqual(
            emotion_detector("I am afraid")["dominant_emotion"],
            "fear"
        )


if __name__ == "__main__":
    unittest.main()