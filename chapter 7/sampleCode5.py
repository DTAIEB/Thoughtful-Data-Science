schema = StructType(
[StructField(f["name"], f["type"], True) for f in field_metadata]
)
csv_sdf = spark.readStream\
	.format("csv")\
	.option("schema", schema)\
	.option("multiline", True)\
	.option("dateFormat", 'EEE MMM dd kk:mm:ss Z y')\
.option("ignoreTrailingWhiteSpace", True)\
.option("ignoreLeadingWhiteSpace", True)\
	.load(output_dir)
