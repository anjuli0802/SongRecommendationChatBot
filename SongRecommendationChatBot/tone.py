#tone
from textblob import TextBlob

def analyze_tone(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "positive"
    elif sentiment < 0:
        return "negative"
    else:
        return "neutral"

from flask import Blueprint,request
tone = Blueprint('tone', __name__)
# from utility_functions.utils import analyseTone



@tone.route('/api/tone',methods=['POST'])
def getTone():
    msg=request.get_json()
    msg=msg['chat']
    print('In tone analyser message is ',msg)
    tone=analyze_tone(msg)
    print('In tone analyser tone analysed is ',tone)
    return {
        'tone':tone
    }