class StreamsManager():
    def __init__(self):
        self.twitter_stream = None
        self.csv_sdf = None
        
    def reset(self, search_query = None):
        if self.twitter_stream is not None:
            self.twitter_stream.disconnect()
        #stop all the active streaming queries and re_initialize the directories
        for query in spark.streams.active:
            query.stop()
        # initialize the directories
        self.root_dir, self.output_dir = init_output_dirs()
        # start the tweepy stream
        self.twitter_stream = start_stream([search_query]) if search_query is not None else None
        # start the spark streaming stream
        self.csv_sdf = start_streaming_dataframe(output_dir) if search_query is not None else None
        
    def __del__(self):
        # Automatically called when the class is garbage collected
        self.reset()
        
streams_manager = StreamsManager()
