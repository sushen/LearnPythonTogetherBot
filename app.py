import sys
from flask import Flask, request
from pprint import pprint
from utils import wit_response
from pymessenger import Bot, Element

app = Flask(__name__)

# Facebook apps link:   https://developers.facebook.com/apps/2222049801408664/dashboard/
FB_ACCESS_TOKEN = "EAAfk8UkWEJgBAIIX1hzUoRXZA4OWlh7QjLeA5nCmS9bTWzbOwyiZBUqqX9ZAWPlihNFSqBoKVtDQVx0YaR9zFtP8j8UUsLahjmvLipWAQgZBW1p6BlvMp1VlVY6INjblCUUZAAUWjJ7a4c1uGcAY6bOjPPcerFF1P2JfCKCQVdAZDZD"
bot = Bot(FB_ACCESS_TOKEN)

VERIFICATION_TOKEN = "hello"


@app.route('/', methods=['GET'])
def verify():
    # Web hook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log(data)

    # **Necessary Code that extract json data facebook send**
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

                    # # Echo Bot
                    # response = messaging_text
                    # bot.send_text_message(sender_id, response)

                    # greetings_response = {"payload": {
                    #     "template_type": "button",
                    #     "text": "What do you want to do next?",
                    #     "buttons": [
                    #         {
                    #             "type": "web_url",
                    #             "url": "https://www.messenger.com",
                    #             "title": "Visit Messenger"
                    #         },
                    #
                    #     ]
                    # },
                    # }

                    # replace Echo Bot to wit ai
                    response = None

                    entity, value = wit_response(messaging_text)

                    if entity == 'greetings':
                        elements = []
                        element = Element(title="test", image_url="<arsenal_logo.png>", subtitle="subtitle",
                                          item_url="http://arsenal.com")
                        elements.append(element)

                        bot.send_generic_message(recipient_id, elements)


                    elif entity == 'thanks':
                        response = " Thank you too"
                        bot.send_text_message(sender_id, response)

                    if response == None:
                        # response = "We are testing"
                        # bot.send_text_message(sender_id, response)
                        elements = []
                        element = Element(title="test", image_url="<arsenal_logo.png>", subtitle="subtitle",
                                          item_url="http://arsenal.com")
                        elements.append(element)

                        bot.send_generic_message(recipient_id, elements)

    return "ok", 200


def log(message):
    # previously it was print now I just Use Petty Print
    pprint(message)
    sys.stdout.flush()


if __name__ == "__main__":
    app.run(port=80, use_reloader=True)
