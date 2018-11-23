import os, sys
from flask import Flask, request
from utils import wit_response, get_news_elements
from utilsforSimpleMassage import wit_response
from pymessenger import Bot, Element, Button
from fbmq import Attachment, Template, QuickReply, Page

from pprint import pprint

# from pymessenger2.bot import Bot
# from pymessenger2 import Element

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
    return "Hello World", 200


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
                    # add for image reply
                    elif 'text' in messaging_event['message']:
                        messaging_text = messaging_event['message']['attachments']

                    else:
                        messaging_text = 'no text'

                    response = None
                    entity, value = wit_response(messaging_text)

                    if entity == 'greetings':
                        Page.send(self(), recipient_id=sender_id, message="hello world!")

    # # .........From Wit * this work and bring Generic template...........
                    # categories = wit_response(messaging_text)
                    # elements = get_news_elements(categories)
                    # bot.send_generic_message(sender_id, elements)

                    # # Echo Bot
                    # response = messaging_text
                    # bot.send_text_message(sender_id, response)

                    # replace Echo Bot to wit ai
                    # response = None
                    #
                    # entity, value = wit_response(messaging_text)
                    #
                    # if entity == 'greetings':


    #........... for Simple text * this thing only work...........

                        # response = " Welcome"
                        # bot.send_text_message(sender_id, response)


    # # ..........For buttons * its not working ..............
    #                     buttons = []
    #                     button = Button(title='Arsenal', type='web_url', url='http://arsenal.com')
    #                     buttons.append(button)
    #                     button = Button(title='Other', type='postback', payload='other')
    #                     buttons.append(button)
    #                     text = 'Select'
    #                     bot.send_button_message(recipient_id, text, buttons)
    #                     result = bot.send_button_message(recipient_id, text, buttons)
    #                     assert type(result) is dict
    #                     assert result.get('message_id') is not None
    #                     assert result.get('recipient_id') is not None

    # # ..........For Image * its not working ..............
    #                     image_url = "https://www.pexels.com/photo/nature-summer-purple-yellow-36753/"
    #                     bot.send_image_url(recipient_id, image_url)

    # # ...........For  Generic Template * its not working...........
    #                     elements = []
    #                     element = Element(title="test", image_url="<arsenal_logo.png>", subtitle="subtitle",
    #                                       item_url="http://arsenal.com")
    #                     elements.append(element)
    #
    #                     bot.send_generic_message(recipient_id, elements)

                    elif entity == 'thanks':
                        response = " Thank you too"
                        bot.send_text_message(sender_id, response)

                    if response == None:
                        response = "We are testing"
                        bot.send_text_message(sender_id, response)
                        # image_url = "https://www.pexels.com/photo/nature-summer-purple-yellow-36753/"
                        # bot.send_image_url(recipient_id, image_url)

    return "ok", 200


def log(message):
    # previously it was print now I just Use Petty Print
    pprint(message)
    sys.stdout.flush()


if __name__ == "__main__":
    app.run(port=80, use_reloader=True)
