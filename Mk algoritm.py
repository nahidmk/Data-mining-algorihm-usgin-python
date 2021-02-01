
import numpy as np
from itertools import combinations



def clean_the_data(data ,minimum_support):
    arr =[]
    final = []
    mapper={}
    for i in data:
        for j in i:
            if j in mapper.keys():
                mapper[j] = mapper[j]+1
            else:
                mapper[j]=1

    for item in data:
        s = ""
        item.sort()
        for items in item:
            if mapper[items]>1:
                s += items
        final.append(list(s))
    return final


def Association_rule(clean_data, items_in_bundle):
    table = {}
    for bundle in clean_data:
        item_combination = list(combinations(bundle,items_in_bundle))
        for k in item_combination:
            if k in table.keys():
                table[k] = table[k]+1
            else:
                table[k] = 1
    return table





data = [["A", "B", "C", "D"],
        ["C", "D", "E"],
        ["A", "B"],
        ["A", "C", "D"],
        ["B", "D", "F", "G"]]

minimum_support = 2
items_in_bundle = 2

clean_data = clean_the_data(data,minimum_support)

count_of_item = Association_rule(clean_data,items_in_bundle)

print(count_of_item)