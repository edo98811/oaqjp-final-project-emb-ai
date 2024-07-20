import requests
import json

def emotion_detector(text_to_analyse):
    
    # Set up request
    url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyse } }

    # Make the request
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response)

    # Identify dominant emotion
    emotions_scores = json.reads(response["text"])
    emotions_scores = identify_dominant_emotion(emotion_scores)

def identify_dominant_emotion(emotions):

    best = NA
    for emotion in keys(emotions):
        if best == NA: best == emotion
        else if emotions[emotion] > emotions[emotion]: best = emotion
    
    return (emotions.update({"dominant_emotion": best}))


if __name__ == "__main__":
    emotion_detector("hello I am very happy")