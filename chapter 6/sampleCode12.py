import tempfile
def download_image(url):
   response = requests.get(url, stream=True)
   if response.status_code == 200:
      with tempfile.NamedTemporaryFile(delete=False) as f:
         for chunk in response.iter_content(2048):
            f.write(chunk)
         return f.name
   else:
      raise Exception("Unable to download image: {}".format(response.status_code))
