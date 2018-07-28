import time
[[TweetInsightApp]]
@route(search_query="*")
    def do_search_query(self, search_query):
        streams_manager.reset(search_query)
        start_parquet_streaming_query(streams_manager.csv_sdf)
        while True:
            try:
                parquet_dir = os.path.join(root_dir, "output_parquet")
                self.parquet_df = spark.sql("select * from parquet.`{}`".format(parquet_dir))
                break
            except:
                time.sleep(5)
        return """
<div class="container">
    <div id="header{{prefix}}" class="row no_loading_msg" pd_refresh_rate="5000" pd_target="header{{prefix}}">
        <pd_script>
print("Number of tweets received: {}".format(streams_manager.twitter_stream.listener.tweet_count))
        </pd_script>
    </div>
    <div class="row" style="min-height:300px">
        <div class="col-sm-5">
            <div id="metric1{{prefix}}" pd_refresh_rate="10000" class="no_loading_msg"
                pd_options="display_metric1=true" pd_target="metric1{{prefix}}">
            </div>
        </div>
        <div class="col-sm-5">
            <div id="metric2{{prefix}}" pd_refresh_rate="12000" class="no_loading_msg"
                pd_options="display_metric2=true" pd_target="metric2{{prefix}}">
            </div>
        </div>
    </div>
    
    <div class="row" style="min-height:400px">
        <div class="col-sm-offset-1 col-sm-10">
            <div id="word_cloud{{prefix}}" pd_refresh_rate="20000" class="no_loading_msg"
                pd_options="display_wc=true" pd_target="word_cloud{{prefix}}">
            </div>
        </div>
    </div>
        """
