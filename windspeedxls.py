# # coding=utf-8
# import xlrd
#
# # 文件的名字
# file_name = "D:/Cirrus Wind 1/研究DA和RT哪个好/201801_DA与RT对比/11.xls"
# # 打开文件
# bk = xlrd.open_workbook(file_name)
# # 代开sheet1
# sh = bk.sheet_by_name("201801_1_1#")
# # 获取行数
# row_num = sh.nrows
# row_list = []
# for i in range(1, row_num):
#     # 获取第i行的正行的数据
#     row_data = sh.row_values(i)
#     row_list.append(row_data)
# # 打印每一行的内容，打印出的为列表的形式
# for row in row_list:
#     print(row)

#代码示例:
import pandas as pd
excel_path = 'D:/Cirrus Wind 1/研究DA和RT哪个好/201801_DA与RT对比/201801_1_1#.xls'
d = pd.read_excel(excel_path, sheetname=None)
print(d['201801_1_1#'].example_column_name)