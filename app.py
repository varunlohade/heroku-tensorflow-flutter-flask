from flask import Flask, request, jsonify
app= Flask(__name__)
@app.route('/v1/image/convert_cartoon', method = ['POST'])
def convert_cartoon():
    return "", 200

if __name__ =="__main__":
    app.run(host='0.0.0.0',port=5000)