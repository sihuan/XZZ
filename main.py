from flask import Flask, request
from config import HOST, PORT
from route import ZZRouter
import threading

app = Flask(__name__)

@app.route('/', methods=['POST'])
def whenmsg():
    threading.Thread(target=ZZRouter, args=(request.get_json(),),daemon=True).start()
    # ZZRouter(request.get_json())
    return ''

app.run(host= HOST,port = PORT, debug=True)