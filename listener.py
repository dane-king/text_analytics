from tweepy.streaming import StreamListener
import json


class StdOutListener(StreamListener):
    def on_data(self, data):
        return_obj=dict()

        try:
            data = json.loads(data)
            return_obj['is_truncated']=data['truncated']
            
            if("extended_tweet" in data):
                return_obj['text']=data['extended_tweet']['full_text']
            else:
                return_obj['text']=data['text']
            

            return_obj["quote_count"]: data['quote_count']
            return_obj["reply_count"]: data['reply_count']
            return_obj["retweet_count"]: data['retweet_count']
            return_obj["favorite_count"]: data['favorite_count']
            return_obj["user_mentions"]: data['user_mentions']['screen_name']
            print(json.dumps(return_obj))
        except:
            print(json.dumps(data))
            #exit()
        # print(data)
        return True

    def on_error(self, status):
        print (status)