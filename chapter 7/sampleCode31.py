import sys
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, SentimentOptions, EntitiesOptions

# init() function will be called once on pipeline initialization
# @state a Python dictionary object for keeping state. The state object is passed to the process function
def init(state):
    # do something once on pipeline initialization and save in the state object
    state["nlu"] = NaturalLanguageUnderstandingV1(
        version='2017-02-27',
        username='XXXX’,
        password='XXXX'
    )
