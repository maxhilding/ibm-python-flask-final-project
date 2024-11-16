"""This module contains the flask server"""

from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

"""This is the emotionDetector handler"""
@app.route('/emotionDetector')
def emotion_detection():
    """This function returns a string of the emotions \
    in the text"""
    text_to_analyze = request.args.get('text')
    emotions = emotion_detector(text_to_analyze)
    dominant_emotion = emotions['dominant_emotion']
    if dominant_emotion is None:
        return 'Invalid text! Please try again!'
    del emotions['dominant_emotion']
    return f'For the given statement, the system response is \
    {str(emotions)[1:-1]}. The dominant emotion is \
    {dominant_emotion}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
