from flask import Flask, request, jsonify
from v1.image.cartoongan import cartoongan
from werkzeug.serving import WSGIRequestHandler
from PIL import Image
app= Flask(__name__)
@app.route('/v1/image/convert_cartoon', methods = ['POST'])
def convert_cartoon():
    data = request.get_json()
    if 'image' not in data:
        return "", 400
    cartoon_img_data= cartoongan.convert(data['image'])
    return cartoon_img_data, 200
@app.route("/")
def index():
    return "<h1>Welcome to orseliyas ml server</h1>"

if __name__ =="__main__":
    WSGIRequestHandler.protocol_version ="HTTP/1.1"
    app.run(host='127.0.0.1',port=5000)
