from bs4 import BeautifulSoup as BS
import re

# return an array of all the images scraped from an html page
def get_image_urls(url):
    # Instantiate a BeautifulSoup parser
    soup = BS(requests.get(url).text, "html.parser")
    
    # Local helper method for extracting url
    def extract_url(val):
        m = re.match(r"url\((.*)\)", val)
        val = m.group(1) if m is not None else val
        return "http:" + val if val.startswith("//") else val
    
    # List comprehension that look for <img> elements and backgroud-image styles
    return [extract_url(imgtag['src']) for imgtag in soup.find_all('img')] + [ \
        extract_url(val.strip()) for key,val in \
        [tuple(selector.split(":")) for elt in soup.select("[style]") \
            for selector in elt["style"].strip(" ;").split(";")] \
            if key.strip().lower()=='background-image' \
        ] 
