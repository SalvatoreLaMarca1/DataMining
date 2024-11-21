
# This program is used to take a dictionary of transactions and compute
# the contingency matrix, confidenc, interest factor, PS factor, and cosine measure
# of a user inputted association rule. {E} -> {C} for example
#
# Author: Salvatore La Marca

import math

txns = dict({
    1: ('A', 'B', 'D', 'E'),
    2: ('B', 'C', 'D'),
    3: ('A', 'B', 'D', 'E'),
    4: ('A', 'C', 'D', 'E'),
    5: ('B', 'C', 'D', 'E'),
    6: ('B', 'D', 'E'),
    7: ('C', 'D'),
    8: ('A', 'B', 'C'),
    9: ('A', 'D', 'E'),
    10: ('B', 'D')
})

for key, value in txns.items():
    print(f"{key}: {value}")
print()

# get association rules {value1} -> {value2}
value1 = input("Enter value1: ")
value2 = input("Enter value2: ")

# number of transactions 
N = len(txns)

# count combinations for contingency matrix
both = 0
first = 0
second = 0
neither = 0

# check if value1 and/or value2 is in key list
hasv1 = False
hasv2 = False


    
for key, value in txns.items():
    hasv1 = False
    hasv2 = False
    
    if value.__contains__(value1):
        hasv1 = True
    if value.__contains__(value2):
        hasv2 = True
        
    if hasv1 and hasv2:
        both += 1
    elif hasv1 and not hasv2:
        first += 1
    elif not hasv1 and hasv2:
        second += 1
    else:
        neither += 1

# totals for contingency matrix
bf = both + first
sn = second + neither
fn = first + neither
bs = both + second
        
print()
print("Contingency Matrix:")
print(f"     | {value2} | not {value2} | Total")
print("--------------------------")
print(f"    {value1}| {both} | {first}     | {bf}")
print("--------------------------")
print(f"not {value1}| {second} | {neither}     | {sn}")
print("--------------------------")
print(f"Total| {bs} | {fn}     |")        
print()
print(f"Confidence: {round((both) / (bf), 3)}")
print()

print("Interest Factor: ")
s_both = N * both
denom = bf * bs
print(f"{s_both} / {denom} = {round(s_both / denom, 3)}")
print()

print("PS Factor: ")
ps_s_both = s_both / 100
ps_bf = bf / 10
ps_bs = bs / 10
ps_calc = round((ps_s_both - ps_bf * ps_bs), 3)
print(f"{ps_s_both} - {ps_bf} * {ps_bs} = {ps_calc}")
print()

print("IS / Cosine Measure: ")
cosine_measure = s_both / math.sqrt(bf * bs)
# cosine_measure / 10 to move decimal point
print(f"{s_both} / sqrt({bf} * {bs}) = {round(cosine_measure / 10, 3)}")
print()