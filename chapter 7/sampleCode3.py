import shutil
def ensure_dir(dir, delete_tree = False):
    if not os.path.exists(dir):
        os.makedirs(dir)
    elif delete_tree:
        shutil.rmtree(dir)
        os.makedirs(dir)
    return os.path.abspath(dir)

root_dir = ensure_dir("output", delete_tree = True)
output_dir = ensure_dir(os.path.join(root_dir, "raw"))
