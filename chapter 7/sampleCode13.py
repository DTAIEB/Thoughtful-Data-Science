field_metadata = [
    {"name": "created_at","type": DateType()},
    {"name": "text", "type": StringType()},
    {"name": "source", "type": StringType(), 
         "transform": lambda s: BS(s, "html.parser").text.strip()
    },
    {"name": "sentiment", "type": StringType()},
    {"name": "entity", "type": StringType()},
    {"name": "entity_type", "type": StringType()}
]
