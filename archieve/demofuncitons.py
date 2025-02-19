from openpyxlfunction import *
import os
import data
from pathlib import Path
# sheetpath = os.getcwd() + "\grouplist.xlsx"
#
# number = totalsheetcount(sheetpath)
# print(number)
# sheetName = allsheetName(sheetpath)
# print(sheetName)
# # writeData(sheetpath, data.job_portal, 2, 3, "done")
# data1 = ["demo1", "demo2", "demo3", "demo4", "demo5"]
# writecol(sheetpath, data.log ,2, data1)
# print("node count "*50)
# print(getRowCount(sheetpath, data.node_portal))
#
# allsheetname = allsheetName(sheetpath)
# sheetcount = totalsheetcount(sheetpath)
# print("*"*80)
# print("sheetcount {0}".format(sheetcount))
# for i in range(2, sheetcount):
#     print(allsheetname[i])
#
# data = readallsheetdata(sheetpath, data.nodejs_portal,3 )
# print("A"*80)
# print(data)
path = Path(__file__).parent /"1"
print(path)