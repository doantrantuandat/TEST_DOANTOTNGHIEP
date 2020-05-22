from mlxtend.frequent_patterns import fpgrowth, apriori
import pandas as pd
import numpy as np
import os
from os.path import dirname, abspath
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import association_rules

dataset = [['f', 'a', 'c', 'd', 'g', 'i', 'm', 'p'],
           ['a', 'b', 'c', 'f', 'l', 'm', 'o'],
           ['b', 'f', 'h', 'j', 'o', 'w'],
           ['b', 'c', 'k', 's', 'p'],
           ['a', 'f', 'c', 'e', 'l', 'p', 'm', 'n']]
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

"""
Apriori
"""
patterns_ap = apriori(df, min_support=0.6, use_colnames=True)
rules_ap = association_rules(
    patterns_ap, metric="confidence", min_threshold=0.6)
rules_ap_sort_descending = rules_ap.sort_values(
    by="confidence", ascending=False)

rules_ap_antecedents_list = list(rules_ap_sort_descending['antecedents'])
rules_ap_consequents_list = list(rules_ap_sort_descending['consequents'])
rules_ap_support_list = list(rules_ap_sort_descending['support'])
rules_ap_confidence_list = list(rules_ap_sort_descending['confidence'])
rules_ap_lift_list = list(rules_ap_sort_descending['lift'])

rules_ap_final = []
for i in range(0, len(rules_ap_antecedents_list)):
    onerules = {}
    onerules['antecedents'] = list(rules_ap_antecedents_list[i])
    onerules['consequents'] = list(rules_ap_consequents_list[i])
    onerules['support'] = rules_ap_support_list[i]
    onerules['confidence'] = rules_ap_confidence_list[i]
    onerules['lift'] = rules_ap_lift_list[i]
    rules_ap_final.append(onerules)
# print(rules_ap_final)
# print("==============================================================")

"""
FP-Growth
"""
patterns_fp = fpgrowth(df, min_support=0.6, use_colnames=True, verbose=0)
rules_fp = association_rules(
    patterns_fp, metric="confidence", min_threshold=0.6)
rules_fp_sort_descending = rules_fp.sort_values(
    by="confidence", ascending=False)
# print(rules_fp_sort_descending)

rules_fp_antecedents_list = list(rules_fp_sort_descending['antecedents'])
rules_fp_consequents_list = list(rules_fp_sort_descending['consequents'])
rules_fp_support_list = list(rules_fp_sort_descending['support'])
rules_fp_confidence_list = list(rules_fp_sort_descending['confidence'])
rules_fp_lift_list = list(rules_fp_sort_descending['lift'])

rules_fp_final = []
for i in range(0, len(rules_fp_antecedents_list)):
    onerules = {}
    onerules['antecedents'] = list(rules_fp_antecedents_list[i])
    onerules['consequents'] = list(rules_fp_consequents_list[i])
    onerules['support'] = rules_fp_support_list[i]
    onerules['confidence'] = rules_fp_confidence_list[i]
    onerules['lift'] = rules_fp_lift_list[i]
    rules_fp_final.append(onerules)
# print(rules_fp_final)
for item in rules_fp_final:
    print(item)
