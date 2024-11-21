# Assignment 2 - Salvatore La Marca

from itertools import combinations

# Transaction dataset
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

# Step 1: Generate frequent 1-itemsets
item_support = {}
for txn in txns.values():
    for item in txn:
        if item not in item_support:
            item_support[item] = 0
        item_support[item] += 1
        
# Filter 1-itemsets by minsup
frequent_1_itemsets = {item: count for item, count in item_support.items() if count >= minsup}

print("\nFrequent 1-itemsets:")
print(frequent_1_itemsets)
print()

# Convert frequent 1-itemsets to a list of single-item tuples for candidate generation
prev_frequent_itemsets = {tuple([item]) for item in frequent_1_itemsets}

# Function to check if all subsets of a candidate are frequent
def has_infrequent_subset(candidate, prev_frequent_itemsets):
    k_subsets = combinations(candidate, len(candidate) - 1)
    for subset in k_subsets:
        if tuple(sorted(subset)) not in prev_frequent_itemsets:
            return True
    return False

# Step 2: Generate frequent k-itemsets (k >= 2)
k = 2
while prev_frequent_itemsets:
    print(f"Generating {k}-itemsets...")
    
    # Generate candidate k-itemsets by joining (k-1)-itemsets with each other
    candidate_k_itemsets = set([tuple(sorted(set(itemset1).union(itemset2))) 
                                for itemset1 in prev_frequent_itemsets 
                                for itemset2 in prev_frequent_itemsets 
                                if len(set(itemset1).union(itemset2)) == k])
    
    # Apply pruning: Keep only those candidates whose (k-1)-subsets are frequent
    candidate_k_itemsets = {itemset for itemset in candidate_k_itemsets if not has_infrequent_subset(itemset, prev_frequent_itemsets)}
    
    # Count support for candidate k-itemsets
    itemset_k_counts = {}
    for txn in txns.values():
        for itemset in candidate_k_itemsets:
            if all(item in txn for item in itemset):
                itemset_k_counts[itemset] = itemset_k_counts.get(itemset, 0) + 1
    
    # Filter k-itemsets by minsup
    frequent_k_itemsets = {itemset: count for itemset, count in itemset_k_counts.items() if count >= minsup}
    
    if frequent_k_itemsets:
        print(f"Frequent {k}-itemsets:")
        print(frequent_k_itemsets)
        print()
    else:
        break  # If no frequent k-itemsets, stop generating further
    
    # Update prev_frequent_itemsets for the next iteration (k+1)
    prev_frequent_itemsets = set(frequent_k_itemsets.keys())
    
    k += 1
