from flask import Flask
from flask import request
import vk_api
import os

app = Flask(__name__)

vk = vk_api.VkApi(token=os.environ['VK_API_ACCESS_TOKEN'])
#vk.auth()

@app.route("/", methods=['POST', 'GET'])
def hello():
    if request.method == 'GET':
        # Default hujeta
        return "This is bot!"
    else:
        # Real logic
        requestJson = request.get_json(force=True)

        if requestJson['type'] == 'message_new':
            userId = request['object']['from_id']
            vk.method('message.send', {'user_id': userId, 'message': 'Pashol nahui'})
        else:
            return "Unsupported request type"

        return "Some logic ebat'"
