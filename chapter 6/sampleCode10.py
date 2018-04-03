# Load the labels
def load_labels(model, as_json = False):
    labels = [line.rstrip() \
      for line in requests.get(get_url(model, model["label_file"]) ).text.split("\n") if line != ""]
    if as_json:
        return [{"index": item.split(":")[0],"label":item.split(":")[1]} for item in labels]
    return labels
