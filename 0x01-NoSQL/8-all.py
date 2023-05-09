#!/usr/bin/env python3
'''File for Task 8.
'''


def list_all(mongo_collection):
    '''lists all documents in a collection.
    '''
    return [doc for doc in mongo_collection.find()]

