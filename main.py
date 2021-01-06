from moviepy.editor import *
from flask import *
import flask
import urllib
import urllib.request
import firebase_admin
from firebase_admin import storage, credentials
import os
from datetime import date


app = Flask(__name__)

#### http://127.0.0.1:5000/url?url1:url1&&url2=url2
@app.route('/')
def process():
    return "Hello"


def process_video(ip_address):
    list_of_video = []

    clip = VideoFileClip(ip_address+"1.mp4")
    list_of_video.append(clip)

    clip = VideoFileClip(ip_address+"2.mp4")
    list_of_video.append(clip)

    final_clip = concatenate_videoclips(list_of_video)
    final_clip.write_videofile(ip_address+"new.mp4")


@app.route('/url', methods=['GET'])
def get_query_string():
    ip_address = flask.request.remote_addr
    message = (request.query_string).decode("utf-8")
    i = message.index("url1:")
    j = message.index("url2")

    url1 = message[i + 5:j - 2]
    url2 = message[j + 5:]

    urllib.request.urlretrieve(url1, ip_address+"1.mp4")
    urllib.request.urlretrieve(url2, ip_address+"2.mp4")
    if not firebase_admin._apps:
        cred = credentials.Certificate("fir-tuturial-a30a1-firebase-adminsdk-otqp0-5bd3729283.json")
        firebase_admin.initialize_app(cred, {'storageBucket': 'fir-tuturial-a30a1.appspot.com'})

    process_video(ip_address)
    fileName = ip_address+"new.mp4"

    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

    # Opt : if you want to make public access from the URL
    blob.make_public()

    print("fir-tuturial-a30a1.appspot.com", blob.public_url)

    d = {
        "url1": url1,
        "url2": url2,
        "url3": blob.public_url
    }
    # os.remove("demofile.txt")
    os.remove(ip_address+"1.mp4")
    os.remove(ip_address+"2.mp4")
    os.remove(ip_address+"new.mp4")
    print(ip_address)
    return jsonify(d)


if __name__ == '__main__':
    app.run(debug=False)
