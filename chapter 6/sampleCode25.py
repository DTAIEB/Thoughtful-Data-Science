from pixiedust.utils.environment import Environment
root_dir = ensure_dir_exists(os.path.join(Environment.pixiedustHome, "imageRecoApp")
image_dir = root_dir
image_dict = get_url_for_keywords(["apple", "orange", "pear", "banana"])
with open(os.path.join(image_dir, "retrained_label.txt"), "w") as f_label: 
    for key in image_dict:
        f_label.write(key + "\n")
        path = ensure_dir_exists(os.path.join(image_dir, key))
        count = 0
        for url in image_dict[key]:
            download_image_into_dir(url, path)
            count += 1
            if count > 500:
                break;
