# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tweepy
import json
from twitter_stream import RecentSearch
from twitter_stream import SampledStream
from twitter_stream import FilteredStream

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    consumer_key = "vdBZ7nsubfElOYBk0X7kqFbKo"
    consumer_secret = "g6QX0iihsSpD1Mx2ojuF8sZq7VgO86B4cCyruptd4hlcYofRw8"
    access_token = "821329451757793280-SRq3NIonOCEJVDyMHzNqvZXePQavSHN"
    access_token_secret = "EBhi9fFocHDt8rsWKYWNypCK3K2DhSdov653L6zk8iwHy"


    rules: list = [
        {"value": "place:\"George Bush Intercontinental Airport (IAH)\" has:geo", "tag": "IAH"}
    ]

    # deletelist = {
    #         "delete": {
    #             "ids": ['1475932361049190408'] # example id
    #         }
    #     }
    class Stream(FilteredStream):
        user_fields = ['name', 'location', 'public_metrics']
        expansions = ['author_id']
        tweet_fields = ['created_at', 'geo']

    stream = Stream()
    stream.add_rule(data={"add": rules})
    # stream.delete_rule(data=deletelist)
    print(stream.get_rules())


for tweet in stream.connect():
    print(json.dumps(tweet, indent=4))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
