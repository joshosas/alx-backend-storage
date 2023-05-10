#!/usr/bin/env python3
'''File for Task 11.
'''


def schools_by_topic(mongo_collection, topic):
    '''returns a list of school with a specific topic.
    '''
    filter_topics = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(filter_topics)]
