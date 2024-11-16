import requests
import json
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    obj = {"raw_document": {"text": text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=obj, headers=header)
    emotions = json.loads(response.text)['emotionPredictions'][0]['emotion']
    print(emotions)
    dominant_emotion = {'emotion': '', 'value': 0}
    for key, val in emotions.items():
        if float(val) > dominant_emotion['value']:
            dominant_emotion['emotion'] = key
            dominant_emotion['value'] = float(val)
    relevant_emotions = {'anger': emotions['anger'],
    'disgust': emotions['disgust'],
    'fear': emotions['fear'],
    'joy': emotions['joy'],
    'sadness': emotions['sadness'],
    'dominant_emotion': dominant_emotion['emotion']}
    return relevant_emotions