# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from twitter_stream import FilteredStream
import time
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rules: list = [
        {"value": "place:\"Purdue University Airport (LAF)\" has:geo", "tag": "PUA"}
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

while True:

    try:
        for tweet in stream.connect():
            with open('output.txt', 'a') as f:
                print(json.dumps(tweet), file=f)
            print(tweet)

    except:
        print("no tweet collected")
        time.sleep(1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
