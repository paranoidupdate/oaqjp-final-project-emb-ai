import requests

URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
EMOTIONS = ["anger", "disgust", "fear", "joy", "sadness"]

def emotion_detector(text_to_analyze):
    data = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(URL, json=data, headers=HEADERS)

    if response.status_code == 200:
        response = response.json()
        emotions = response["emotionPredictions"][0]["emotion"]

        # Identify dominant emotion
        dominant_score = 0
        dominant_emotion = "joy"

        for emotion, score in emotions.items():
            if score >= dominant_score:
                dominant_score = score
                dominant_emotion = emotion
        emotions["dominant_emotion"] = dominant_emotion
        return emotions

    if response.status_code == 400:
        emotions = {emotion: None for emotion in EMOTIONS}
        emotions["dominant_emotion"] = None
        return emotions
