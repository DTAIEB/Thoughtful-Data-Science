[[TweetInsightApp]]
@route(display_metric1="*")
    def do_display_metric1(self, display_metric1):
        parquet_dir = os.path.join(root_dir, "output_parquet")
        self.parquet_df = spark.sql("select * from parquet.`{}`".format(parquet_dir))
        return """
<div class="no_loading_msg" pd_render_onload pd_entity="parquet_df">
    <pd_options>
    {
      "legend": "true",
      "keyFields": "sentiment",
      "clusterby": "entity_type",
      "handlerId": "barChart",
      "rendererId": "bokeh",
      "rowCount": "10",
      "sortby": "Values DESC",
      "noChartCache": "true"
    }
    </pd_options>
</div>
        """
