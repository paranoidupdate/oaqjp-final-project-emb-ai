"""Web emotion detector"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def index():
    """Main page"""
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_handler():
    """Emotion detector request handler"""
    text_to_analyze = request.args["textToAnalyze"]
    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    response = (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response

if __name__ == "__main__":
    app.run(debug=True)
