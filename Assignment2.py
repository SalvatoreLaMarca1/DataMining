
# Dictionary for transactions

from itertools import combinations
import math


txns = dict({
    1: ('Milk', 'Beer', 'Diapers'),
    2: ('Bread', 'Butter', 'Milk'),
    3: ('Milk', 'Diapers', 'Cookies'),
    4: ('Bread', 'Butter', 'Cookies'),
    5: ('Beer', 'Cookies', 'Diapers'),
    6: ('Milk', 'Diapers', 'Bread', 'Butter'),
    7: ('Bread', 'Butter', 'Diapers'),
    8: ('Beer', 'Diapers'),
    9: ('Milk', 'Diapers', 'Bread', 'Butter'),
    10: ('Beer', 'Cookies')
})


# Minimum support threshold
minsup = 3

# Count support of individual items
item_support = {}

for txn in txns.values():
    for item in txn:
        if item not in item_support:
            item_support[item] = 0
        item_support[item] += 1

# Filter items by minsup
frequent_items = {item: count for item, count in item_support.items() if count >= minsup}

print()

print("Frequent 1-itemsets:")

for item in frequent_items:
    print(f"{item}: {frequent_items.get(item)}")


print()

print("Here is the number of combinations")

items = 4
itemCount = 2

num_combinations = math.comb(items, itemCount)
print(num_combinations)

print()

unique_items = set()
for txn in txns.values():
    unique_items.update(txn)
    
# Generate all possible 2-itemsets from the unique items
frequent_2_itemsets = list(combinations(unique_items, 2))

# print all 2-itemsets
num = 1

print("Possible 2-itemsets")

print(frequent_2_itemsets)
    
    
# Generate frequent itemsets for 2-itemsets
itemset_counts = {}

# Generate all possible 2-itemsets and get support counts
for txn in txns.values():
    for itemset in combinations(txn, 2):
        itemset = tuple(sorted(itemset))
        if itemset not in itemset_counts:
            itemset_counts[itemset] = 0
        itemset_counts[itemset] += 1
        
# Filter 2-itemsets by minimum support
frequent_itemsets = {itemset: count for itemset, count in itemset_counts.items() if count >= minsup}


# Minimum support threshold
minsup = 3

# Step 1: Count support for 1-itemsets
def count_single_items(txns):
    item_support = {}
    for txn in txns.values():
        for item in txn:
            if item not in item_support:
                item_support[item] = 0
            item_support[item] += 1
    return item_support

# Step 2: Count support for k-itemsets
def count_k_itemsets(txns, k_itemsets):
    itemset_counts = {}
    for txn in txns.values():
        for itemset in k_itemsets:
            if set(itemset).issubset(set(txn)):  # Check if itemset is a subset of the transaction
                itemset = tuple(sorted(itemset))
                if itemset not in itemset_counts:
                    itemset_counts[itemset] = 0
                itemset_counts[itemset] += 1
    return itemset_counts

# Step 3: Filter itemsets based on minsup
def filter_itemsets_by_minsup(itemsets, minsup):
    return {itemset: count for itemset, count in itemsets.items() if count >= minsup}

# Step 4: Generate candidate k-itemsets from frequent (k-1)-itemsets
def generate_candidate_itemsets(frequent_itemsets, length):
    items = set()
    for itemset in frequent_itemsets.keys():
        items.update(itemset)
    return list(combinations(items, length))

# Step 5: Apriori Algorithm to find frequent 1-itemsets, 2-itemsets, and 3-itemsets
# Step 5a: Find frequent 1-itemsets
single_item_support = count_single_items(txns)
frequent_1_itemsets = filter_itemsets_by_minsup(single_item_support, minsup)

# Step 5b: Find frequent 2-itemsets from frequent 1-itemsets
candidate_2_itemsets = generate_candidate_itemsets(frequent_1_itemsets, 2)
counted_2_itemsets = count_k_itemsets(txns, candidate_2_itemsets)
frequent_2_itemsets = filter_itemsets_by_minsup(counted_2_itemsets, minsup)


# Step 5c: Find frequent 3-itemsets from frequent 2-itemsets
candidate_3_itemsets = generate_candidate_itemsets(frequent_2_itemsets, 3)
counted_3_itemsets = count_k_itemsets(txns, candidate_3_itemsets)
frequent_3_itemsets = filter_itemsets_by_minsup(counted_3_itemsets, minsup)

print("\n")
# Output the results

# Step 1: Generate candidate 3-itemsets by joining 2-itemsets
def generate_candidate_3_itemsets(frequent_2_itemsets):
    candidate_3_itemsets = set()
    for itemset1 in frequent_2_itemsets:
        for itemset2 in frequent_2_itemsets:
            if itemset1 != itemset2:
                # Find the union of two itemsets if they share a common item
                union_set = set(itemset1).union(set(itemset2))
                if len(union_set) == 3:  # Only consider itemsets of size 3
                    candidate_3_itemsets.add(tuple(sorted(union_set)))
    return candidate_3_itemsets

# Step 2: Prune candidate 3-itemsets (only keep those whose 2-item subsets are all frequent)
def prune_candidates(candidate_3_itemsets, frequent_2_itemsets):
    pruned_3_itemsets = set()
    for itemset in candidate_3_itemsets:
        valid = True
        for subset in combinations(itemset, 2):  # Check all 2-item subsets
            if tuple(sorted(subset)) not in frequent_2_itemsets:
                valid = False
                break
        if valid:
            pruned_3_itemsets.add(itemset)
    return pruned_3_itemsets

# Step 3: Count support for candidate 3-itemsets in transactions
def count_3_itemsets(txns, candidate_3_itemsets):
    itemset_counts = {}
    for txn in txns.values():
        for itemset in candidate_3_itemsets:
            if set(itemset).issubset(set(txn)):  # Check if itemset is a subset of the transaction
                itemset = tuple(sorted(itemset))
                if itemset not in itemset_counts:
                    itemset_counts[itemset] = 0
                itemset_counts[itemset] += 1
    return itemset_counts


# Step 4: Filter 3-itemsets by minsup
def filter_itemsets_by_minsup(itemsets, minsup):
    return {itemset: count for itemset, count in itemsets.items() if count >= minsup}

# Execute the steps
candidate_3_itemsets = generate_candidate_3_itemsets(frequent_2_itemsets)
pruned_3_itemsets = prune_candidates(candidate_3_itemsets, frequent_2_itemsets)
counted_3_itemsets = count_3_itemsets(txns, pruned_3_itemsets)
frequent_3_itemsets = filter_itemsets_by_minsup(counted_3_itemsets, minsup)

# Output the frequent 3-itemsets
print("Frequent 3-itemsets with minsup 3:")
for itemset, count in frequent_3_itemsets.items():
    print(f"{itemset}: {count}")
    
#Generate candidate 4-itemsets by joining 3-itemsets
def generate_candidate_4_itemsets(frequent_3_itemsets):
    candidate_4_itemsets = set()
    for itemset1 in frequent_3_itemsets:
        for itemset2 in frequent_3_itemsets:
            if itemset1 != itemset2:
                union_set = set(itemset1).union(set(itemset2))
                if len(union_set) == 3:
                    candidate_4_itemsets.add(tuple(sorted(union_set)))
    return candidate_4_itemsets

# Prune candidate 4-itemsets (only keep those whose 3-item subsets are all frequent)
def prune_candidates_4(candidate_4_itemsets, frequent_3_itemsets):
    pruned_4_itemsets = set()
    for itemset in candidate_4_itemsets:
        valid = True
        for subset in combinations(itemset, 2): # check all 3-item subsets
            if tuple(sorted(subset)) not in frequent_3_itemsets:
                valid = False
                break;
        if valid:
            pruned_4_itemsets.add(itemset)
    return pruned_4_itemsets

    
# candidate 4-itemsets in transactions
def count_4_itemsets(txns, candidate_4_itemsets):
    itemset_counts = {}
    for txn in txns.values():
        for itemset in candidate_4_itemsets:
            if set(itemset).issubset(set(txn)):
                itemset = tuple(sorted(itemset))
                if itemset not in itemset_counts:
                    itemset_counts[itemset] = 0
                itemset_counts[itemset] += 1
    return itemset_counts
    

# Attempting to do 4-itemsets by minsup
def filter_itemsets_by_minsup(itemsets, minsup):
    return {itemset: count for itemset, count in itemsets.items() if count >= minsup}

candidate_4_itemsets = generate_candidate_4_itemsets(frequent_3_itemsets)
pruned_4_itemsets = prune_candidates(candidate_4_itemsets, frequent_3_itemsets)
counted_4_itemsets = count_4_itemsets(txns, pruned_4_itemsets)
frequent_4_itemsets = filter_itemsets_by_minsup(counted_4_itemsets, minsup)


# Output the frequent 4-itemsets
print("Frequent 4-itemsets with minsup 3:")
for itemset, count in frequent_4_itemsets.items():
    print(f"{itemset}: {count}")


# # Assignment 2 - Salvatore La Marca

# from itertools import combinations
# import math

# # transaction dataset
# txns = dict({
#     1: ('Milk', 'Beer', 'Diapers'),
#     2: ('Bread', 'Butter', 'Milk'),
#     3: ('Milk', 'Diapers', 'Cookies'),
#     4: ('Bread', 'Butter', 'Cookies'),
#     5: ('Beer', 'Cookies', 'Diapers'),
#     6: ('Milk', 'Diapers', 'Bread', 'Butter'),
#     7: ('Bread', 'Butter', 'Diapers'),
#     8: ('Beer', 'Diapers'),
#     9: ('Milk', 'Diapers', 'Bread', 'Butter'),
#     10: ('Beer', 'Cookies')
# })

# # Minimum support threshold
# minsup = 3

# # The support of each item
# item_support = {}

# # Loop through and add all the support values to each item type
# for txn in txns.values():
#     for item in txn:
#         if item not in item_support:
#             item_support[item] = 0
#         item_support[item] += 1
        
# # Check for frequent items based on minsup
# frequent_1_itemsets = {item: count for item, count in item_support.items() if count >= minsup}

# print("\nFrequent 1-itemsets:")
# print(frequent_1_itemsets)
# print()


# unique_items = set()
# for txn in txns.values():
#     unique_items.update(txn)
    
# # Generate all possible 2-itemsets from unique items
# possible_2_itemsets = list(combinations(unique_items, 2))

# print("Possible 2-itemsets:")
# print(possible_2_itemsets)
# print()
    
    
# # Support counts for itemset 2
# itemset_2_counts = {}

# for txn in txns.values():
#     for itemset in combinations(txn, 2):
#         itemset = tuple(sorted(itemset))
#         if itemset not in itemset_2_counts:
#             itemset_2_counts[itemset] = 0
#         itemset_2_counts[itemset] += 1
        
# # Filter 2-itemsets by minsup
# frequent_2_itemsets = {itemset: count for itemset, count in itemset_2_counts.items() if count >= minsup}
 
# print("Frequent 2-itemsets:")           
# print(frequent_2_itemsets)
