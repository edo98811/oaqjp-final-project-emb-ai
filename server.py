"""
server.py

This module sets up a Flask web server for emotion detection. It provides two routes:
- The '/emotionDetector' route that accepts GET requests to 
  analyze text input and return emotion scores.

Dependencies:
- Flask: A web framework used to create the web server and handle HTTP requests.
- emotion_detector: A custom module used to detect emotions from text input.

The server responds to GET requests with JSON data 
containing emotion scores and the dominant emotion.
"""
from flask import Flask, request, jsonify
import emotion_detector as ed


app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector():
    """Detect emotions from the provided text."""

    data = request.json
    text_to_analyze = data.get('text', '')

    # Check if the input text is empty
    if not text_to_analyze.strip():
        # Create a response with all None values for the emotion scores
        error_response = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

        response_message = "Error: No input provided. Please enter some text for analysis."
        response_body = jsonify({'status_code': 400, 'message': \
            response_message, 'data': error_response})

        return response_body, 400

    emotion_scores = ed.emotion_detector(text_to_analyze)

    # If no dominant emotion
    if emotion_scores.get('dominant_emotion', 0) is None:
        return jsonify({'message': "Invalid text! Please try again!"})

    # Format the response message
    response_message = (f"For the given statement, the system response is "
                        f"anger: {emotion_scores.get('anger', 0)}, "
                        f"disgust: {emotion_scores.get('disgust', 0)}, "
                        f"fear: {emotion_scores.get('fear', 0)}, "
                        f"joy: {emotion_scores.get('joy', 0)}, "
                        f"sadness: {emotion_scores.get('sadness', 0)}. "
                        f"The dominant emotion is {emotion_scores.get('dominant_emotion', 0)}.")

    return jsonify({'message': response_message})


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
