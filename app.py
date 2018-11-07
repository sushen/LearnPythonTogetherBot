import sys
from flask import Flask, request
from pprint import pprint
from pymessenger import Bot

app = Flask(__name__)

FB_ACCESS_TOKEN = "EAADrJVpQGToBAHvbQvZBhgRgqjYCeSQdvobiOX6GO8bvlJ8iIR1aFIRLSVZCIbSREjObUzDB9As2ySVHZCSYWbiky2PZBCMeh2plVHEb4ZCAETuNvJXOZAoHuejEcFFQC628lzjXGAjWXZAJTgDwxXFYFvUojl4rOgZAxuK91ZATZCPQZDZD"
bot = Bot(FB_ACCESS_TOKEN)

VERIFICATION_TOKEN = "hello"


@app.route('/', methods=['GET'])
def verify():
    # Web hook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "App Creat By Sushen Biswas To Know more Please Contact Sushen Biswas", 200


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log(data)

    return "ok", 200


def log(message):
    pprint(message)
    sys.stdout.flush()


if __name__ == "__main__":
    app.run(use_reloader=True)
