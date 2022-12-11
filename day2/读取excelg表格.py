# @Time: 2022/12/11 17:55
import pandas as pd
path = r'C:\Users\fzh00\Desktop\文件\excel\1. Excel基础操作\课后练习1：月度考勤.xlsx'
df = pd.read_excel(path,'员工信息')
print(type(df))
print(df)
