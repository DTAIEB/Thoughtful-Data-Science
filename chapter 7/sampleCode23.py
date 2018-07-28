import matplotlib.pyplot as plt
from wordcloud import WordCloud
[[TweetInsightApp]]
@route(display_wc="*")
@captureOutput
def do_display_wc(self):
    text = "\n".join(
        [r['entity'] for r in self.parquet_df.select("entity").collect() if r['entity'] is not None]
    )
    plt.figure( figsize=(13,7) )
    plt.axis("off")
    plt.imshow(
        WordCloud(width=750, height=350).generate(text), 
        interpolation='bilinear'
    )
