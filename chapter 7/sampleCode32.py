# @event a Python dictionary object representing the input event tuple as defined by the input schema
# @state a Python dictionary object for keeping state over subsequent function calls
# return must be a Python dictionary object. It will be the output of this operator.
# Returning None results in not submitting an output tuple for this invocation.
# You must declare all output attributes in the Edit Schema window.
def process(event, state):
    # Enrich the event, such as by:
    # event['wordCount'] = len(event['phrase'].split())
    try:
        event['text'] = event['text'].replace('"', "'")
        response = state["nlu"].analyze( 
            text = event['text'],
            features=Features(sentiment=SentimentOptions(), entities=EntitiesOptions())
        )
        event["sentiment"] = response["sentiment"]["document"]["label"]
        top_entity = response["entities"][0] if len(response["entities"]) > 0 else None
        event["entity"] = top_entity["text"] if top_entity is not None else ""
        event["entity_type"] = top_entity["type"] if top_entity is not None else ""
    except Exception as e:
        return None
    return event
