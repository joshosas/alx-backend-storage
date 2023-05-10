#!/usr/bin/env python3
'''File for Task 14.
'''


def top_students(mongo_collection):
    '''returns all students sorted by average score.
    '''
    sorted_students = mongo_collection.aggregate(
        [
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'averageScore': {
                        '$avg': {
                            '$avg': '$topics.score',
                        },
                    },
                    'topics': 1,
                },
            },
            {
                '$sort': {'averageScore': -1},
            },
        ]
    )
    return sorted_students
