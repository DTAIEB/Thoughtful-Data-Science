parquet_batch_df = spark.sql(
"select * from parquet.`{}`".format(
os.path.join(root_dir, "output_parquet")
)
)
