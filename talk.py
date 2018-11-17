def talking():
    # ** How I emplement a list in function

    templates = {
        "recipient": {
            "id": "<PSID>"
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": "What do you want to do next?",
                    "buttons": [
                        {
                            "type": "web_url",
                            "url": "https://www.messenger.com",
                            "title": "Visit Messenger"
                        },
                        {
                            ...
                        },
                        {...}
                    ]
                }
            }
        }
    }
    elements = []
    for template in templates:
        element = {
        "recipient": {
            "id": "<PSID>"
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": "What do you want to do next?",
                    "buttons": [
                        {
                            "type": "web_url",
                            "url": "https://www.messenger.com",
                            "title": "Visit Messenger"
                        },
                        {
                            ...
                        },
                        {...}
                    ]
                }
            }
        }
    }
        elements.append(element)
    return elements


print(talking())

# fruits = [{"template_type": "generic", "elements": [  "GENERIC_TEMPLATE",  "GENERIC_TEMPLATE" , ...]}]
# for fruit in fruits:
#      print(fruit)
