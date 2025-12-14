import unittest

from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        input_output = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear"
        }
        for input_, output in input_output.items():
            self.assertEqual(
                emotion_detector(input_)["dominant_emotion"],
                output
            )

if __name__ == "__main__":
    unittest.main()