from gnewsclient import gnewsclient
from pprint import pprint


# clint = gnewsclient()
#
# clint.query = "Environment Bay of bangla"
# news_client = clint.get_news()
# pprint(news_client[0])


# def get_news_elements(categories):
#     news_client = gnewsclient()
#     news_client.query = ''
#
#     news_items = news_client.get_news()
#
#     elements = []
#
#     for item in news_items:
#         element = {
#             'title': item['title'],
#             'buttons': [{
#                 'type': 'web_url',
#                 'title': "Read more",
#                 'url': item['link']
#             }],
#             'image_url': item['img']
#         }
#         elements.append(element)
#
#     return elements
#
#
# pprint(get_news_elements('sports'))

#Data I have
Data = [{'buttons': [{'title': 'Read more',
               'type': 'web_url',
               'url': 'https://www.washingtonpost.com/politics/happy-thanksgiving-to-all-rhetorical-bedlam-erupts-as-president-trump-speaks-to-the-world-from-mar-a-lago/2018/11/22/349c4a3e-ee7d-11e8-96d4-0d23f2aaad09_story.html'}],
  'image_url': 'https://t2.gstatic.com/images?q=tbn:ANd9GcTZuqREXUg5LpjaRxRqzMXHt3lJ4AtZwmN4_Q0j5wuF0zfFmP_FII0tZDsqfOmgFRJb9J6ckeLB',
  'title': "'HAPPY THANKSGIVING TO ALL!': Rhetorical bedlam erupts as "
           'President Trump speaks to the world from Mar-a-Lago - Washington '
           'Post'},
 {'buttons': [{'title': 'Read more',
               'type': 'web_url',
               'url': 'https://www.nytimes.com/2018/11/22/us/politics/trump-saudi-thanksgiving.html'}],
  'image_url': 'https://t1.gstatic.com/images?q=tbn:ANd9GcRx_abBGoj1N7xaKk_5fo4K4IruqrH5Cb0dbGvL3fppPewLBj6d91y91Dzj5y2C8AZ0zTuIMtSZ',
  'title': "Rebuffing CIA, Trump Says It Only Has 'Feelings' About Khashoggi "
           'Killing - New York Times'},
 {'buttons': [{'title': 'Read more',
               'type': 'web_url',
               'url': 'https://www.nytimes.com/2018/11/22/world/europe/hillary-clinton-migration-populism-europe.html'}],
  'image_url': 'https://t1.gstatic.com/images?q=tbn:ANd9GcRC5jjCQUwyKB5UtnqpzJWHqtXOwtrEQn2eZbzw4QCIlshWpDfY1lt_tBbXP-zf1IrwdUM_Ey_sIA',
  'title': "Hillary Clinton Says Europe Must 'Get a Handle' on Migration to "
           'Thwart Populism - New York Times'},
 {'buttons': [{'title': 'Read more',
               'type': 'web_url',
               'url': 'https://www.bostonglobe.com/metro/2018/11/22/cold-temperatures-set-regional-records-for-thanksgiving/f9XPnnJUpPuJc15I8P1uWP/story.html'}],
  'image_url': 'https://t2.gstatic.com/images?q=tbn:ANd9GcTmt8RptBnpemFCM7oAoOA8itbV9MLWYBNSOHStaqWMAikT6SYujlXuvrG0p5fqZTViUQClSDy9',
  'title': 'Cold temperatures set regional records for Thanksgiving - The '
           'Boston Globe'},
 {'buttons': [{'title': 'Read more',
               'type': 'web_url',
               'url': 'https://www.cbssports.com/nfl/news/chicago-bears-vs-detroit-lions-score-live-updates-game-stats-highlights-for-thanksgiving-nfl-game/'}],
  'image_url': 'https://t2.gstatic.com/images?q=tbn:ANd9GcRPewAelgX-GcSmynwLPEMIJvej04kfSdkDTui4eJ4fpVhjXMdJZlLisggETopNyktkGuRUYYrt',
  'title': 'Chicago Bears vs. Detroit Lions score: Live updates, game stats, '
           'highlights for Thanksgiving NFL game - CBSSports.com'},
 {'buttons': [{'title': 'Read more',
               'type': 'web_url',
               'url': 'https://www.bustle.com/p/the-live-action-lion-king-trailer-recreates-a-iconic-moment-from-the-animated-film-video-13188580'}],
  'image_url': 'https://t3.gstatic.com/images?q=tbn:ANd9GcS_JYjs0HpxaN5jmhp5k4QYTHQI6A6ky_aG2Dn9axj-52c08y3f48FGu10-zN94yGkdZNpEvM1L',
  'title': "The Live-Action 'Lion King' Trailer Recreates A Iconic Moment From "
           'The Animated Film — VIDEO - Bustle'},
 {'buttons': [{'title': 'Read more',
               'type': 'web_url',
               'url': 'https://www.cnn.com/2018/11/22/asia/afghan-child-sales-intl/index.html'}],
  'image_url': 'https://t0.gstatic.com/images?q=tbn:ANd9GcRoHIxBrVeb1A4mUxgdEENV8Eknpp6GJthorObbMepufkuWL00ZzZYA3e-6ztrieL8xe4HfsFwA',
  'title': "Mother had 'no other choice' but to sell her 6-year-old daughter - "
           'CNN'},
 {'buttons': [{'title': 'Read more',
               'type': 'web_url',
               'url': 'https://www.npr.org/2018/11/22/670268418/milwaukee-girl-who-condemned-gun-violence-is-killed-by-bullet'}],
  'image_url': 'https://t0.gstatic.com/images?q=tbn:ANd9GcQxNfBrer1X88lfTDY77bLfhs9pepS8gLXDIfsUkKluDV87PiYtObilEadh3dw1jBcvqSIaBlY9',
  'title': 'Milwaukee Girl Who Condemned Gun Violence Is Killed By Bullet - '
           'NPR'},
 {'buttons': [{'title': 'Read more',
               'type': 'web_url',
               'url': 'http://www.nfl.com/news/story/0ap3000000991383/article/dak-prescottamari-cooper-combo-fuels-cowboys-win'}],
  'image_url': 'https://t3.gstatic.com/images?q=tbn:ANd9GcR7Qvh5MfNa-XbGTZIPjKKNb-Nzt3nIDDWBzS-WPs24yb2XVm8ZagDZ9kXJQxkt28bYngZKYUkb',
  'title': "Dak Prescott-Amari Cooper combo fuels Cowboys' win - NFL.com"},
 {'buttons': [{'title': 'Read more',
               'type': 'web_url',
               'url': 'https://www.bustle.com/p/the-shoes-alexandria-ocasio-cortez-wore-while-campaigning-just-became-a-part-of-history-13188287'}],
  'image_url': 'https://t3.gstatic.com/images?q=tbn:ANd9GcRKBM4hf5fJiXYXs5hTxU-LyftjH6cWoSp6uFfZhbwPxVS8_bXi7QBB3Z2ru_4BVV2F1kSYdR_J',
  'title': 'The Shoes Alexandria Ocasio-Cortez Wore While Campaigning Just '
           'Became A Part Of History - Bustle'}]

# new experiment
news_items = Data

elements = []

for item in news_items:
    element = {
        'title': item['title'],
        'buttons': [{
            'type': 'web_url',
            'title': "Read more",
            'url': item['link']
        }],
        'image_url': item['img']
    }
    elements.append(element)

print(elements)
