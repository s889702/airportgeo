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
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""


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
