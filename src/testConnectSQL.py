import pyodbc
import os
from mlxtend.frequent_patterns import association_rules
from mlxtend.frequent_patterns import fpgrowth, apriori
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import time
server = "DESKTOP-JR11ETH\SQLEXPRESS"
database = "AdventureWorks2012"
username = "sa"
password = "sapassword"


conn = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};'
                      f'Server=' + server+';'
                      f'Database='+database+';'
                      f'UID='+username+';'
                      f'PWD='+password+';'
                      'Mars_Connection=Yes;')
cursor = conn.cursor()


getSaleProduct = cursor.execute(
    'SELECT SalesOrderID,SalesOrderDetailID, [Production].[Product].[ProductID], Name FROM [Sales].[SalesOrderDetail] inner join [Production].[Product] on [Production].[Product].[ProductID] = [Sales].[SalesOrderDetail].[ProductID] order by [Sales].[SalesOrderDetail].SalesOrderID asc')

# # len = 0
# # for i in getSaleProduct:
# #     len = len + 1
# #     # print(i)
# # print(len)

listSaleProduct = []
for saleProduct in getSaleProduct:
    listSaleProduct.append(list(saleProduct))

list_saleProduct_parent = []
list_saleProduct_child = []
temp = listSaleProduct[0][0]
i = 0
while i < len(listSaleProduct):
    if listSaleProduct[i][0] == temp:
        list_saleProduct_child.append(str(listSaleProduct[i][3]))
        i += 1
    else:
        list_saleProduct_parent.append(list_saleProduct_child)
        list_saleProduct_child = []
        temp = listSaleProduct[i][0]
        i = i


# print(list_saleProduct_parent)
# print(len(list_saleProduct_parent))

te = TransactionEncoder()
te_ary = te.fit(list_saleProduct_parent).transform(list_saleProduct_parent)
df = pd.DataFrame(te_ary, columns=te.columns_)

# # time
# start_time = time.clock()
# #
# # apriori
#
# # end time to calculation
# end_time = time.clock()
# time_apriori = (end_time-start_time)/60
# apriori_decimals = "%.2f" % round(time_apriori,2)
# print("\n\nCompleted in %s minutes\n" % apriori_decimals)
start_time = time.clock()*1000
print("At the beginning of the calculation")
print("Processor time (in miliseconds):", start_time, "\n")
patterns_ap = apriori(df, min_support=0.01, use_colnames=True)
end_time = time.clock()
time_apriori = (end_time-start_time)*1000
print("\nAt the end of the calculation")
print("Processor time (in miliseconds):", end_time)
print("Time elapsed during the calculation:", time_apriori)

# print(patterns_ap)
# rules_ap = association_rules(patterns_ap, metric="confidence", min_threshold=0.2)
# rules_ap_sort_descending = rules_ap.sort_values(by="confidence", ascending=False)
# print(rules_ap_sort_descending)
# # print(rules_ap)
# cursor.close()
