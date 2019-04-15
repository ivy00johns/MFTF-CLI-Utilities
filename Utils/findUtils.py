import collections
from collections import Counter

def findDuplicates(listOfItems):
    nodeCounts = collections.Counter(listOfItems)
    duplicatesList = []

    for nodeCount in nodeCounts:
        if (nodeCounts[nodeCount] > 1):
            duplicatesList.append([nodeCount,nodeCounts[nodeCount]])

    return duplicatesList