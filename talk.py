def talking():
    # ** How I emplement a list in function

    templates = [{"title": "Visit Messenger"},
                 {"type": "web_url"},
                 {"url": "https://www.messenger.com"
                  }]
    for template in templates:
        return template


print(talking())

# fruits = [{"template_type": "generic", "elements": [  "GENERIC_TEMPLATE",  "GENERIC_TEMPLATE" , ...]}]
# for fruit in fruits:
#      print(fruit)
