# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 22:14:44 2024

@author: rshar
"""
# Dictionary for transactions
txns = dict({1:('Milk','Bread'),2:('Bread','Butter','Coke'),3:('Milk','Butter')})



# Dictionary for storing support count of items
dict1 = {}

######### Approach - 1: Starting with transactions

for key in txns:            # Loop works 3 times
    items = txns.get(key)
    print(items)
    for i in items:         # Loop works for the count of items (7) on each txn
        print(i) 
        dict1[i] = 0
        # Compute support for i - scan the complete table/dictionary
        
        for val in txns:    # Loop works 3 times
            itemset = txns.get(val)
            if i in itemset:
                dict1[i] += 1
        print(dict1)
print(dict1)      

######### Approach - 2: Starting with unique Items
  
'''
set1 = set()

for key in txns:                # Loop works 3 times
    items = txns.get(key)
    set2 = set(items)
    set1 = set1.union(set2)

print(set1)

for i in set1:                  # Loop works 4 times
    dict1[i] = 0
    for val in txns:            # Loop works 3 times
        itemset = txns.get(val)
        if i in itemset:
            dict1[i] += 1
    print(dict1)
print(dict1)
'''