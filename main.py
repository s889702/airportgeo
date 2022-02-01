# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from twitter_stream import FilteredStream
import json
import time
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rules: list = [
        {"value": "place:\"Purdue University Airport\" has:geo", "tag": "PUA"},
        {"value": "place:\"Boston Logan International Airport\" has:geo", "tag": "BOS"},
        {"value": "place:\"Dallas Love Field\" has:geo", "tag": "DAL"},
        {"value": "place:\"Ontario International Airport\" has:geo", "tag": "ONT"},
        {"value": "place:\"Akron-Canton Airport\" has:geo", "tag": "CAK"},
        {"value": "place:\"Jacksonville Albert J Ellis Airport\" has:geo", "tag": "OAJ"}
    ]

    # deletelist = {
    #         "delete": {
    #             "ids": ['1487972196735717378'] # example id
    #         }
    #     }
    class Stream(FilteredStream):
        user_fields = ['name', 'location', 'public_metrics']
        expansions = ['author_id']
        tweet_fields = ['created_at', 'geo']

    stream = Stream()
    stream.add_rule(data={"add": rules})
    #stream.delete_rule(data=deletelist)
    print(stream.get_rules())

while True:

    try:
        for tweet in stream.connect():
            print(tweet)
            with open('test.txt', 'a') as f:
                print(json.dumps(tweet), file=f)


    except:
        print("no tweet collected")
        time.sleep(1)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
