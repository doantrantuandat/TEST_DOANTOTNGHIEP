## This uses pyfim from http://www.borgelt.net/pyfim.html

# and the dataset from https://www.kaggle.com/puneetbhaya/online-retail


# Importing the libraries
import numpy as np
import pandas as pd
from fim import eclat, apriori, fpgrowth
import time
from datetime import timedelta


# help(eclat)


######## Data Preprocessing
dataset = pd.read_excel('Online Retail.xlsx')
# print(dataset)
#Replace null descriptions with the stock code 
for i, d in dataset[dataset['Description'].isnull()].iterrows():
    dataset['Description'][i] = "Code-" + str(d['StockCode'])
# group into baskets
grouped = dataset.groupby('InvoiceNo')

#rearrange into a list
transactions = []
for name,group in grouped:
    transactions.append(list(group['Description'].map(str)))

# print(transactions)
print('len Transactions: ',len(transactions))
# ##### Training

start_time = time.clock()
report = eclat(tracts=transactions, report='l,C', target='r', supp=5, zmin=1,conf=30)
end_time = time.clock()


print('Len rules: ', len(report))
for i in report:
    print(i[1])
# report.sort(key = lambda x: x[6], reverse = True)
print(timedelta(seconds=end_time - start_time))
##compare with apriori from same module. Different from apyori.... maybe have to investigate further
# from fim import apriori
# help(apriori)
# areport = apriori(transactions, report='l,c', target='r', supp=1, zmin=2)