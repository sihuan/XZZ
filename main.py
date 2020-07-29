from flask import Flask, request
from config import PORT
from route import ZZRouter

app = Flask(__name__)

@app.route('/', methods=['POST'])
def whenmsg():
    ZZRouter(request.get_json())
    return ''

app.run(host='0.0.0.0',port = PORT, debug=True)

