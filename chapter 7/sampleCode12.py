[[RawTweetsListener]]
def enrich(self, data):
    try:
        response = nlu.analyze( 
            text = data['text'],
            features = Features(
                sentiment=SentimentOptions(), 
                entities=EntitiesOptions()
            )
        )
        data["sentiment"] = response["sentiment"]["document"]["label"]
        top_entity = response["entities"][0] if len(response["entities"]) > 0 else None
        data["entity"] = top_entity["text"] if top_entity is not None else ""
        data["entity_type"] = top_entity["type"] if top_entity is not None else ""
        return data
    except Exception as e:
        self.warn("Error from Watson service while enriching data: {}".format(e))
