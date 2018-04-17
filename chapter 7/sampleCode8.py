tweet_streaming_query = csv_sdf.writeStream\
  .outputMode("append")\
  .format("console")\
  .trigger(processingTime='2 seconds')\
  .start()
