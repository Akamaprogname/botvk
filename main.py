from flask import Flask, abort
from flask import request
import vk_api
import os

app = Flask(__name__)

vk = vk_api.VkApi(token=os.environ['VK_API_ACCESS_TOKEN'])


@app.route("/", methods=['POST', 'GET'])
def hello():
    if request.method == 'GET':
        return "This is bot!"
    else:
        # Real logic
        request_json = request.get_json(force=True)

        if request_json['type'] == 'message_new':
            user_id = request_json['object']['user_id']
            vk.method('message.send', {'user_id': user_id, 'message': 'Pashol nahui'})
            return 'ok'
        elif request_json['type'] == 'confirmation':
            return os.environ['CALLBACK_API_CONFIRMATION_TOKEN']
        else:
            return "Unsupported request type"

        return "Some logic ebat'"