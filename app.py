from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
from main import *
import urllib.parse
app = Flask(__name__)
CORS(app)


@app.route('/ImageToVideo/<path:image_urls>', methods=['GET'])
#images is a string of urls separated by commas
def createVideo(image_urls):
    name = "story"
    # Decode the URL-encoded string
    
    print("printing out:")
    print(type(image_urls))
    # Split the decoded URLs into a list
    
    #create image folders
    list_to_images(image_urls)
    #gives exact name of video file (with .mp4)
    video = create_video("images",name)
    url = get_video_url(video)
    clear("images")  
    remove_video(video)
    return url 

if __name__=='__main__':
    app.run(debug=True)