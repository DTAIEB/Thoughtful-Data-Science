model = models['mobilenet']
graph = load_graph(model)
image_urls = get_image_urls("https://www.flickr.com/search/?text=cats")
for url in image_urls:
    results = score_image(graph, model, url)
    print("Result for {}: \n\t{}".format(url, results))
