from pyspark.sql.types import StringType, DateType
from bs4 import BeautifulSoup as BS
field_metadata = [
    {"name": "created_at","type": DateType()},
    {"name": "text", "type": StringType()},
    {"name": "source", "type": StringType(), 
         "transform": lambda s: BS(s, "html.parser").text.strip()
    }
]
