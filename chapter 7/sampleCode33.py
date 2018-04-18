def start_streaming_dataframe():
    "Start a Spark Streaming DataFrame from a Kafka Input source"
    schema = StructType(
        [StructField(f["name"], f["type"], True) for f in field_metadata]
    )
    kafka_options = {
        "kafka.ssl.protocol":"TLSv1.2",
        "kafka.ssl.enabled.protocols":"TLSv1.2",
        "kafka.ssl.endpoint.identification.algorithm":"HTTPS",
        'kafka.sasl.mechanism': 'PLAIN',
        'kafka.security.protocol': 'SASL_SSL'
    }
    return spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", ",".join(message_hub_creds["kafka_brokers_sasl"])) \
        .option("subscribe", "enriched_tweets") \
        .load(**kafka_options)
