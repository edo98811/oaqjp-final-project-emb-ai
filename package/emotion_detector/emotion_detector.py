import requests
import json

def emotion_detector(text_to_analyse):
    
    # Set up request
    url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyse } }

    # Make the request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check for response status code
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
 
        # response = dict()

        # emotions_scores = {
        #     'anger': 0.94,
        #     'disgust': 0.94,
        #     'fear': 0.94,
        #     'joy': 0.95,
        #     'sadness': 0.94
        # }
        # Identify dominant emotion
    emotions_scores = json.reads(response["text"])

    return identify_dominant_emotion(emotions_scores) 

def identify_dominant_emotion(emotions):

    best = None
    for emotion in emotions.keys():
        if best == None: best = emotion
        elif emotions[emotion] > emotions[best]: best = emotion

    emotions["dominant_emotion"] = best

    return emotions


if __name__ == "__main__":
    emotion_detector("hello I am very happy")