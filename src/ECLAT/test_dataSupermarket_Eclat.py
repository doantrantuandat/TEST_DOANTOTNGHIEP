import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from os.path import dirname, abspath
from fim import eclat, apriori, fpgrowth
import time
from datetime import timedelta

# help(fpgrowth)
# help(apriori)


BASE_DIR = dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(str(BASE_DIR), "data\store_data.xlsx")
store_data = pd.read_excel(path, header=None)
print(len(store_data))
# print(store_data)
records = []
for i in range(0, len(store_data)):
    records.append([str(store_data.values[i, j])
                    for j in range(0, len(store_data.columns))])

records_withoutNan = []
for i in range(0, len(records)):
    new = []
    for j in range(0, len(records[i])):
        if str(records[i][j]) != "nan":
            new.append(str(records[i][j]))
    records_withoutNan.append(new)

minsupp = 3
minconf = 10



# Apriori
start_time_ap = time.clock()
rules_ap = apriori(records_withoutNan, report='S,C,l',target='r', supp=minsupp, conf=minconf, mode='o', zmin=2)
end_time_ap = time.clock()
rules_ap.sort(key=lambda x: x[6], reverse=True)
# print(len(rules_ap))
# for i in rules_ap:
#     print(i)
rules_ap_final = []
for i in range(0, len(rules_ap)):
    onerules = {}
    # temp = rules_ap[i][0]
    # temp_antecedents = []
    # temp_antecedents.append(temp)
    onerules['antecedents'] = rules_ap[i][0]
    onerules['consequents'] = list(rules_ap[i][1])
    onerules['support'] = round(rules_ap[i][2], 3)
    onerules['confidence'] = round(rules_ap[i][4], 3)
    onerules['lift'] = round(rules_ap[i][6], 3)
    rules_ap_final.append(onerules)
for i in rules_ap_final:
    print(i)


# # Fp-growth
# start_time_fp = time.clock()
# rules_fp = fpgrowth(records_withoutNan, report='S,C,l',target='r', supp=minsupp, conf=minconf, mode='o', zmin=2)
# end_time_fp = time.clock()
# rules_fp.sort(key=lambda x: x[6], reverse=True)
# # print(len(rules_fp))
# # for i in rules_fp:
# #     print(i)


# # Eclat
# start_time_eclat = time.clock()
# rules_eclat = eclat(records_withoutNan, report='S,C,l',target='r', supp=minsupp, conf=minconf, mode='o', zmin=2)

# # print(len(rules_eclat))
# rules_eclat.sort(key=lambda x: x[6], reverse=True)
# end_time_eclat = time.clock()
# # for i in rules_eclat:
# #     print(i)

# # rules_eclat_1 = eclat(records_withoutNan, target='s',
# #                       report='s', supp=5, conf=10, mode='o', zmin=2, zmax=2)
# # f = open('outfile.txt', 'w')
# # for i in rules_eclat_1:
# #         f.write(str(i[0][0]) + ',' + str(i[0][1]) +'\n')
# # f.close()

# # Max Clique

# rules_eclat_1 = eclat(records_withoutNan, target='s',
#                       report='s', supp=minsupp, conf=minconf, mode='o')

# frequent_itemset_len_1 = []
# for i in rules_eclat_1:
#     if len(i[0]) == 1:
#         frequent_itemset_len_1.append(i)                 

# item = []
# for i in frequent_itemset_len_1:
#     item_child = {}
#     item_child['item'] = i[0][0]
#     item_child['support'] = i[1]
#     item.append(item_child)
# # print('===========================================================================')

# rules_maxClique = []
# start_time_maxEclique = time.clock()
# maxEclique = eclat(records_withoutNan,target='m', report='s', supp=minsupp, conf=minconf, zmin=2, mode='y')
# end_time_maxEclique = time.clock()
# for i in maxEclique: # i: (('nonfat milk', 'spaghetti'), 0.003332888948140248)
#     for j in i[0]: # j: 'nonfat milk' or 'spaghetti'

#         list_except_index = list(i[0])
#         list_except_index.pop(list_except_index.index(j))
#         for k in item: # k: {'item': 'mineral water', 'support': 0.23836821757099053}
#             if j == k['item']:
#                 conf = float(i[1] / k['support'])
#                 if conf >= (10/100):
#                     rules_temp_child = []
#                     rules_temp_child.append(list_except_index)
#                     rules_temp_child.append(j)
#                     rules_temp_child.append(i[1])
#                     rules_temp_child.append(conf)
#                     rules_maxClique.append(rules_temp_child)
#                     break
        
#         list_except_index = list(i[0])


# # for i in rules_temp:
# #     print(i)


# print('len rule apriori: ',len(rules_ap))
# # for i in rules_ap: print(i)
# print('===========================================================================')

# print('len rule eclat: ',len(rules_eclat))
# # for i in rules_eclat: print(i)
# print('===========================================================================')

# print('len rule fp growth : ',len(rules_fp))
# # for i in rules_fp: print(i)
# print('===========================================================================')

# print('len rule max clique: ',len(rules_maxClique))
# # for i in rules_maxClique: print(i)



# print('Apriori time: ', timedelta(seconds=end_time_ap - start_time_ap))
# print('eclat time: ', timedelta(seconds=end_time_eclat - start_time_eclat))
# print('MaxClique time: ', timedelta(seconds=end_time_maxEclique - start_time_maxEclique))
# print('FP-growth time: ', timedelta(seconds=end_time_fp - start_time_fp))


