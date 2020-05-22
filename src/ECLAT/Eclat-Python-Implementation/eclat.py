import numpy as np, itertools
import pandas as pd
import matplotlib.pyplot as plt
import os
from os.path import dirname, abspath
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import association_rules
from mlxtend.frequent_patterns import eclat


np.random.seed(1)
kot = 0
FreqItems = dict()
support = dict()


def eclat(prefix, items, dict_id):
    while items:
        i,itids = items.pop()
        isupp = len(itids)
        if isupp >= minsup:

            FreqItems[frozenset(prefix + [i])] = isupp
            suffix = []
            for j, ojtids in items:
                jtids = itids & ojtids
                if len(jtids) >= minsup:
                    suffix.append((j,jtids))

            dict_id += 1
            eclat(prefix+[i], sorted(suffix, key=lambda item: len(item[1]), reverse=True), dict_id)

def rules(FreqItems, confidence):
    Rules = []
    cnt = 0

    for items, support in FreqItems.items():
        if (len(items) > 1):
            all_perms = list(itertools.permutations(items, len(items)))
            for lst in all_perms:
                antecedent = lst[:len(lst) - 1]
                consequent = lst[-1:]

                conf = float(FreqItems[frozenset(items)]/FreqItems[frozenset(antecedent)]*100)
                if (conf >= confidence):
                    cnt += 1
                    lift = float(conf/FreqItems[frozenset(consequent)])
                    if lift >= 1:
                        Rules.append((antecedent, consequent, support, conf, lift))


    print('Found %d Rules ' % (cnt))
    return Rules


def getantecendent(FreqItems, confidence):
    ant = []
    cnt = 0

    for items, support in FreqItems.items():
        if(len(items) > 1):
            all_perms = list(itertools.permutations(items, len(items)))
            for lst in all_perms:
                antecedent = lst[:len(lst) - 1]
                consequent = lst[-1:]

                conf = float(FreqItems[frozenset(items)]/FreqItems[frozenset(antecedent)]*100)
                if (conf >= confidence):
                    cnt += 1
                    lift = float(conf/FreqItems[frozenset(consequent)])
                    if lift >= 1:
                        ant.append((antecedent))

    print('Print %d attributes' % (cnt))
    return ant

def print_Frequent_Itemsets(output_FreqItems, FreqItems):
    file = open(output_FreqItems, 'w+')
    for item, support in FreqItems.items():
        file.write(" {} : {} \n".format(list(item), round(support,4)))

def print_Rules(output_Rules, Rules):
    file = open(output_Rules, 'w+')
    for a, b,supp, conf, lift in sorted(Rules):
        file.write("{} ==> {} support: {} confidence: {} \n".format((a), (b), round(supp, 4),round(conf, 4),round(lift, 4)))
    file.close()
    
def print_Antecendent(ant):
    file = open('output_antecendent.csv', 'w+')
    for a in sorted(ant):
        file.write("[] \n".format((a)))
    file.close()
    
def Read_Data(filename, delimiter=','):
    data = {}
    trans = 0
    f = open(filename, 'r', encoding="utf8")
    # f = pd.read_excel(path, header=None)
    for row in f:
        trans += 1
        for item in row.split(delimiter):
            if item not in data:
                data[item] = set()
            data[item].add(trans)
    f.close()
    return data

if __name__ == "__main__":
    minsup   = 10
    confidence = 75
    output_FreqItems = 'output_freqitems.csv'
    output_Rules = 'output_rule.csv'
    dict_id = 0

    
    # data = Read_Data('test.xlsx', ',') #change the delimiter based on your input file
    # data.pop("\n",None)
    # data.pop("",None)
    print('finished reading data..... \n Starting mining .....')

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # print(BASE_DIR)
    path = os.path.join(str(BASE_DIR), "test.xlsx")
    store_data = pd.read_excel(path, header=None)

    print(len(store_data))
    records = []
    for i in range(0, len(store_data)):
        records.append([str(store_data.values[i, j]) for j in range(0, 8)])

    records_withoutNan = []
    for i in range(0, len(records)):
        new = []
        for j in range(0, len(records[i])):
            if str(records[i][j]) != "nan":
                new.append(str(records[i][j]))
        records_withoutNan.append(new)
    # print(records_withoutNan)
    te = TransactionEncoder()
    te_ary = te.fit(records_withoutNan).transform(records_withoutNan)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    print(df)

    eclat([], sorted(data.items(), key=lambda item: len(item[1]), reverse=True), dict_id)


    # print('found %d Frequent items' % len(FreqItems))
    # Rules = rules(FreqItems, confidence)
    # print('Writing Rules .....')



    # print_Frequent_Itemsets(output_FreqItems, FreqItems)
    # print_Rules(output_Rules, Rules)
    # Antecendent = getantecendent(FreqItems, confidence)
    # print_Antecendent(Antecendent)
    
    # Ant1d = np.hstack(Antecendent)
    
    # count = np.array(Ant1d)
    # unique, counts = np.unique(count, return_counts=True)
    # dict(zip(unique, counts))
    # counted = np.stack((unique, counts), axis=1)
    # appendFile = open('candidate.csv','w')
    # for i in range(0,len(counted)):
    #     appendFile.write(str(unique[i])+";"+str(counts[i])+","+"\n")
    # appendFile.close()
    
    # df = pd.DataFrame(counted, columns=['word','counter'])
    # df["counter"] = pd.to_numeric(df["counter"])
    # sortcounted = df.sort_values(["counter"], axis=0, 
    #                  ascending=[False]) 
    # elimcounted = sortcounted.drop(sortcounted[sortcounted['counter']<2].index)
    
    # listfrequent = list(elimcounted.iloc[:, 0].values)
    

