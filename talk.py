from wit import Wit
from gnewsclient import gnewsclient

access_token = "OXUVKGL5TU7HIERIGBPWEVKCFIFBLRQK"

client = Wit(access_token=access_token)


def talking(message_text):
    resp = client.message(message_text)
    categories = {'greetings': None}

    entities = list(resp['entities'])
    for entity in entities:
        categories[entity] = resp['entities'][entity][0]['value']

    return categories


def template(categories):
    news_clint = gnewsclient()
    news_clint.query = ''

    if categories['greetings'] != None:
        news_clint.query += categories['greetings'] + ' '

    news_items = news_clint.get_news()
    elements = []

    for item in news_items:
        element = {
            'title': item['title'],
            'buttons': [{
                'type': 'web_url',
                'title': 'Read more',
                'url':item['link']
            }],
            'image_url':item['img']
        }
        elements.append(element)

    return elements


#print(template(talking("hello")))
