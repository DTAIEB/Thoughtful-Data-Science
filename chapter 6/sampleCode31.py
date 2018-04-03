# classify an image given its url
def score_image(graph, model, url):
    # Download the image and build a tensor from its data
    t = read_tensor_from_image_file(model, download_image(url))
    
    def do_score_image(graph, output_layer, labels):        
        # Retrieve the tensors corresponding to the input and output layers
        input_tensor = graph.get_tensor_by_name("import/" + input_layer + ":0");
        output_tensor = graph.get_tensor_by_name( output_layer + ":0");

        with tf.Session(graph=graph) as sess:
         	  # Initialize the variables
            sess.run(tf.global_variables_initializer())
            results = sess.run(output_tensor, {input_tensor: t})
        results = np.squeeze(results)
        # select the top 5 candidates and match them to the labels
        top_k = results.argsort()[-5:][::-1]
        return [(labels[i].split(":")[1], results[i]) for i in top_k]
    
    results = {}
    input_layer = get_model_attribute(model, "input_layer", "input")
    labels = load_labels(model)
    results["mobilenet"] = do_score_image(graph, "import/" + get_model_attribute(model, "output_layer"), labels)
    if "custom_graph" in model and "custom_labels" in model:
        with open(model["custom_labels"]) as f:
            labels = [line.rstrip() for line in f.readlines() if line != ""]
            custom_labels = ["{}:{}".format(i, label) for i,label in zip(range(len(labels)), labels)]
        results["custom"] = do_score_image(model["custom_graph"], "final_result", custom_labels)
    return results
