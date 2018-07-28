def start_parquet_streaming_query(csv_sdf):
    """
    Create and run a streaming query from a Structured DataFrame 
    outputing the results into a parquet database
    """
    streaming_query = csv_sdf \
      .writeStream \
      .format("parquet") \
      .option("path", os.path.join(root_dir, "output_parquet")) \
      .trigger(processingTime="2 seconds") \
      .option("checkpointLocation", os.path.join(root_dir, "output_chkpt")) \
      .start()
    return streaming_query
