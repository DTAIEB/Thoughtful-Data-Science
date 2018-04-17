tweet_streaming_query = csv_sdf \
  .writeStream \
  .format("parquet") \
  .option("path", os.path.join(root_dir, "output_parquet")) \
  .trigger(processingTime="2 seconds") \
  .option("checkpointLocation", os.path.join(root_dir, "output_chkpt")) \
  .start()
