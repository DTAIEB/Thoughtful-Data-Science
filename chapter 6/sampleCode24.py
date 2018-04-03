def get_url_for_keywords(keywords):
    results = {}
    for keyword in keywords:
        df = wnid_to_words.loc[wnid_to_words['description'] == keyword]
        row_list = df['wnid'].values.tolist()
        descriptions = df['description'].values.tolist()
        if len(row_list) > 0:
            results[descriptions[0]] = wnid_to_urls.loc[wnid_to_urls['wnid'] == row_list[0]]["url"].values.tolist()
    return results
