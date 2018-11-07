import sys
from flask import Flask, request
from pprint import pprint
from pymessenger import Bot
from utils import wit_response

app = Flask(__name__)

FB_ACCESS_TOKEN = "EAADrJVpQGToBAHvbQvZBhgRgqjYCeSQdvobiOX6GO8bvlJ8iIR1aFIRLSVZCIbSREjObUzDB9As2ySVHZCSYWbiky2PZBCMeh2plVHEb4ZCAETuNvJXOZAoHuejEcFFQC628lzjXGAjWXZAJTgDwxXFYFvUojl4rOgZAxuK91ZATZCPQZDZD"
bot = Bot(FB_ACCESS_TOKEN)

VERIFICATION_TOKEN = "hello"


@app.route('/', methods=['GET'])
def verify():
    # this block of code is for Web hook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "App Creat By Sushen Biswas To Know more Please Contact Sushen Biswas", 200


# this is for posting massage to the log in json format
@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log(data)

    # Necessary Code that extract json data facebook send
    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:

                # IDs
                sender_id = messaging_event['sender']['id']
                recipient_id = messaging_event['recipient']['id']

                if messaging_event.get('message'):
                    # Extracting text message
                    if 'text' in messaging_event['message']:
                        messaging_text = messaging_event['message']['text']
                    else:
                        messaging_text = 'no text'

                    # replace Echo Bot to wit ai
                    response = None

                    entity, value = wit_response(messaging_text)
                    if entity == 'newstype':
                        response = "Ok, I will send you the {} news".format(str(value))
                    elif entity == 'location':
                        response = "Ok, so you live in {0}. Here are top headlines from {0}".format(str(value))

                    if response == None:
                        response = "Sorry, I didnt understand"

                    bot.send_text_message(sender_id, response)
    return "ok", 200


# this for print nice log and its need pymessenger library
def log(message):
    pprint(message)
    sys.stdout.flush()


if __name__ == "__main__":
    app.run(use_reloader=True)
