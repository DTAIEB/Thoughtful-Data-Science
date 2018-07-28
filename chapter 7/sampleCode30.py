[[RawTweetsListener]]
def on_data(self, data):
    self.tweet_count += 1
    self.producer.send(
        self.topic, 
        {key:transform(key,value) \
                for key,value in iteritems(json.loads(data)) \
                if key in fieldnames}
    )
    return True
