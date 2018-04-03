import numpy as np

# classify an image given its url
def score_image(graph, model, url):
    # Get the input and output layer from the model
    input_layer = get_model_attribute(model, "input_layer", "input")
    output_layer = get_model_attribute(model, "output_layer")
    
    # Download the image and build a tensor from its data
    t = read_tensor_from_image_file(model, download_image(url))
    
    # Retrieve the tensors corresponding to the input and output layers
    input_tensor = graph.get_tensor_by_name("import/" + input_layer + ":0");
    output_tensor = graph.get_tensor_by_name("import/" + output_layer + ":0");

    with tf.Session(graph=graph) as sess:
        results = sess.run(output_tensor, {input_tensor: t})
    results = np.squeeze(results)
    # select the top 5 candidate and match them to the labels
    top_k = results.argsort()[-5:][::-1]
    labels = load_labels(model)
    return [(labels[i].split(":")[1], results[i]) for i in top_k]
