import sys
from flask import Flask, request, render_template
from utils import wit_response
from pymessenger import Bot, Element, Button


app = Flask(__name__)
from pprint import pprint


app = Flask(__name__)

# Facebook apps link:   https://developers.facebook.com/apps/2222049801408664/dashboard/
FB_ACCESS_TOKEN = "EAAfk8UkWEJgBAAhogYdoIsWGuYuh11xkHI27d3Y1rDPBGMLDvH3MVZBJIgWo3bqHqPdKutZAvTrLDTsByQD1pr2kOApZAwHjiW24nIH28PHTaqs8xFTrADuJQD8XuRwMlRzaDPyxEE26dfgJtecRb9a7AbIdy7ZAVoSud6cxZBZBAHXF4haEZCf"

bot = Bot(FB_ACCESS_TOKEN)

VERIFICATION_TOKEN = "hello"

@app.route('/', methods=['GET'])
def verify():
    # Web hook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return render_template("index.html")


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
                        response = " hi, How Can I help you. "
                        bot.send_text_message(sender_id, response)

                    elif entity == 'thanks':
                        response = " thank you too."
                        bot.send_text_message(sender_id, response)

                    # if response == None:
                    #     response = "You Have to type or Kindly Use Our Menu."
                    #     bot.send_text_message(sender_id, response)

    return "ok", 200


@app.route('/Privacy-Policy')
def privacy_policy():
    return render_template("Privacy-Policy.html")


def log(message):
    # previously it was print now I just Use Petty Print
    pprint(message)
    sys.stdout.flush()


if __name__ == "__main__":
    app.run(port=80, use_reloader=True)