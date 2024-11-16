from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def emotionDetector():
    text_to_analyze = request.args.get('text')
    emotions = emotion_detector(text_to_analyze)
    dominant_emotion = emotions['dominant_emotion']
    del emotions['dominant_emotion']
    return f'For the given statement, the system response is {str(emotions)[1:-1]}. The dominant emotion is {dominant_emotion}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)