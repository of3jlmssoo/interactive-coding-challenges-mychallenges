""" result.py
copied from https://github.com/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/utils/results.py
"""
class Results(object):

    def __init__(self):
        self.results = []

    def add_result(self, result):
        # TODO: Clean this up
        # Simplifies challenge coding and unit testing
        # but makes this function look less appealing
        self.results.append(int(str(result)))

    def clear_results(self):
        self.results = []

    def __str__(self):
        return str(self.results)