from flask import Flask, request
from config import HOST, PORT
from route import ZZRouter

app = Flask(__name__)

@app.route('/', methods=['POST'])
def whenmsg():
    ZZRouter(request.get_json())
    return ''

app.run(host= HOST,port = PORT, debug=True)