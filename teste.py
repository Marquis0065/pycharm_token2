import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#一行代码输出统计分析报告
import pandas_profiling as pp
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
import seaborn as sns
from statsmodels.formula.api import ols
from statsmodels.stats.outliers_influence import variance_inflation_factor as vif
# from pyecharts import options as opts
# from pyecharts.charts import Scatter
# from pyecharts.commons.utils import JsCode
# from pyecharts.faker import Faker


#pyecharts画图
# c = Scatter()
# c.add_xaxis(Faker.choose())
# c.add_yaxis(
#         "商家A",
#         [list(z) for z in zip(Faker.values(), Faker.choose())],
#         label_opts=opts.LabelOpts(
#             formatter=JsCode(
#                 "function(params){return params.value[1] +' : '+ params.value[2];}"
#             )
#         ),
#     )
# c.set_global_opts(
#         title_opts=opts.TitleOpts(title="Scatter-多维度数据"),
#         tooltip_opts=opts.TooltipOpts(
#             formatter=JsCode(
#                 "function (params) {return params.name + ' : ' + params.value[2];}"
#             )
#         ),
#         visualmap_opts=opts.VisualMapOpts(
#             type_="color", max_=150, min_=20, dimension=1
#         ),
#     )
# # c.render_notebook();
# c.render("scatter_multi_dimension11140210.html")

# data_raw = pd.read_excel(r"C:\Data\Jupyter_file\统计建模\LR_practice.xlsx")
# #删除无用变量，ID，Acc,edad2
# data_raw.drop(['id','Acc','edad2'],axis=1,inplace=True)
# #缺失值填补，均值或中位数填补，分类变量用众数填补
# #分类变量处理,字符串需要先编码,二分类变量可以直接用map映射方法
# data_raw['gender'] = data_raw['gender'].map({'Male':1,'Female':0})
# #计算均值
# data_raw['avg_exp'].fillna(data_raw['avg_exp'].mean(),inplace=True)
# label = data_raw['edu_class'].unique().tolist()
# data_raw['edu_class'] = data_raw['edu_class'].apply(lambda x:label.index(x))
# #3倍标准差 stats.zscore()
# z_age = stats.zscore(data_raw['Age'])
# #寻找异常数据
# # z_age[(z_age>3)|(z_age<-3)]
# # data_raw['Age'].iloc[40] #引年龄结果是999异常
# #可以用均值代替 data_raw['Age'] 包含异常值，一般不用
# data_raw['Age'].drop(index=40).mean() #去除异常值
# data_raw['Age'].iloc[40] = data_raw['Age'].drop(index=40).mean()
# #哑变量转换 prefic修改列名,drop_first 删除
# dummy = pd.get_dummies(data_raw['edu_class'],prefix='edu',drop_first=True)
# data = pd.concat([data_raw,dummy],axis=1)
#
# #建立模型
# formula = 'avg_exp ~ gender+Age+Income+Ownrent+Selfempl+dist_home_val+dist_avg_income+edu_1+edu_2+edu_3+edu_4'
# #实例化
# model = ols(formula=formula,data = data)
# #拟合模型
# result = model.fit()
#
# #常用接口
# # model.df_resid
# # #调取残差序列
# # result.resid
# # data_vif = data.drop('avg_exp',axis=1)
# # data_vif['Inter'] = 1
# # data_vif.drop(['edu_1','edu_2','edu_3','edu_4'],axis = 1,inplace = True)
# # data_vif.head()
#
# #查看第几个变量的VIF: 1-3,无需处理，3-10，处理，大于10，不可用
# #Income  和dist_avg_Income 删除其中一个
# data2 = data
# data2.drop('Income',axis = 1 ,inplace = True)
# # data2.head()
# # for i in range(0,data_vif.shape[1]):
# #     data_vif.columns[i] , vif(data_vif,i)
#
# #重新拟合模型
# formula2 = 'avg_exp ~ gender+Age+Ownrent+Selfempl+dist_home_val+dist_avg_income+edu_1+edu_2+edu_3+edu_4'
# #实例化
# model2 = ols(formula=formula2,data = data2)
# #拟合模型
# result2 = model2.fit()
#
# #绘制残差图,如果出现叭状，先对Y对对数
# # plt.scatter(result2.predict(data2),result2.resid)
# # #正态性
# # stats.probplot(result2.resid,plot = plt);
#
# #重新拟合模型
# #因变量取对数
# data3 = data2
# data3['ln_avg_exp'] = np.log(data3['avg_exp'])
# formula3 = 'ln_avg_exp ~ gender+Age+Ownrent+Selfempl+dist_home_val+dist_avg_income+edu_1+edu_2+edu_3+edu_4'
# #实例化
# model3 = ols(formula=formula3,data = data3)
# #拟合模型
# result3 = model3.fit()
#
# #加入（年龄）高次项
# data4 = data3
# data4['Age_sq'] = data4['Age']**2
#
# formula4 = 'ln_avg_exp ~ gender+Age_sq+Age+Ownrent+Selfempl+dist_home_val+dist_avg_income+edu_1+edu_2+edu_3+edu_4'
# #实例化
# model4 = ols(formula=formula4,data = data4)
# #拟合模型
# result4 = model4.fit()
#
# #加入（年龄性别）交互项
# data5 = data4
# data5['Age_gender'] = data5['Age']*data5['gender']
#
# formula5 = 'ln_avg_exp ~ gender+Age_sq+Age+Age_gender+Ownrent+Selfempl+dist_home_val+dist_avg_income+edu_1+edu_2+edu_3+edu_4'
# #实例化
# model5 = ols(formula=formula5,data = data5)
# #拟合模型
# result5 = model5.fit()
# #输出结果
# print(result5.summary())







# import random
# d = np.random.randint(1,1000,1000)
# df = pd.DataFrame({'a':d,'b':d*2+1})
# print(df.head())
# result = ols('a~b',df).fit().summary()
# print(result)

# 邮件的标题,需要引入email库中header模块中的Header()函数。
# 邮件的内容,需要引入email库中mime模块下text模块中的MIMEText()函数。
# 邮件的发送者、接收者、服务器地址、端口号、账号、密码等，需要引入smtplib，使用SMTP_SSL()函数。
# while True:
#     from email.header import Header
#     from email.mime.text import MIMEText
#     import smtplib #SMTP协议客户端
#     from  email.mime.multipart import MIMEMultipart
#     import time
#     import pymysql
#     import pandas as pd
#     import xlwings as xw
#     import matplotlib.pyplot as plt
#     import warnings
#     warnings.filterwarnings('ignore')
#     import seaborn as sns
#
#     #设置绘图风格
#     # plt.style.use('seaborn')
#     # #设置字体为黑色
#     # plt.rcParams['font.family']='SimHei'
#     # #显示符号
#     # plt.rcParams['axes.unicode_minus']= False
#
#     #定时发送
#     ehour = 20
#     emin = 4
#     esec = 0
#     #获取当前时间进行对比,当前时区
#     cur_time = time.localtime(time.time())
#     today = time.strftime('%Y%m%d',cur_time)
#     if (cur_time.tm_hour == ehour) and (cur_time.tm_min == emin) and (cur_time.tm_sec == esec):
#         #创建数据库连接
#         print('开始连接数据库。。。')
#         conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='1qaz@WSX',
#                           database='cda3')
#         cur = conn.cursor()
#         sql_cus = 'select * from customer_detail'
#
#         sql_rep = 'select * from repayment_sum_month'
#         customer = pd.read_sql(sql_cus,conn)
#         repay = pd.read_sql(sql_rep,conn)
#
#         #找出逾期数据
#         delay = repay[repay['当前最大逾期天数']>0]
#         #计算账龄并添加逾期数据
#         delay['账龄']=(pd.to_datetime(delay['当前日期']).dt.year-pd.to_datetime(delay['放款日期']).dt.year)*12+\
#                       (pd.to_datetime(delay['当前日期']).dt.month - pd.to_datetime(delay['放款日期']).dt.month)
#         #计算违约金额
#         pivot_delay = pd.pivot_table(delay,index="放款月",columns="账龄",values="剩余本金",aggfunc="sum")
#         # 计算每月的放款总金额
#         customer["年月"] = customer["放款日期"].astype(str).str[:7]
#         gp = customer.groupby("年月").agg({"合同金额": sum})  # 统计每月“通过量”的总量
#         # 计算违约率
#         result = pivot_delay.apply(lambda x: x / gp["合同金额"])
#         # 修改result的列名和插入放款总金额并导出数据
#         result.columns = ['mob_'+str(i) for i in result.columns]
#         result.insert(0, "放款总金额", gp["合同金额"])
#         result.to_excel("result_{}.xlsx".format(today))
#         print("数据导出成功")
#
#         # 绘制图形
#         fig1 = plt.figure(figsize=(10, 5))
#         for i in result.index[1:-1]:
#             plt.plot(result.columns[1:], result.loc[i, "mob_1":])
#         plt.title("逾期数据趋势图")
#         plt.xlabel("账龄")
#         plt.ylabel("逾期率")
#         plt.legend(result.index[1:-1])
#         # 把绘制的图形插入到导出的数据表中
#         app = xw.App(visible=False, add_book=False)
#         book = app.books.open("result_{}.xlsx".format(today))
#         book.sheets.add("折线图", after="Sheet1")  # 新增一个工作表
#         sheet = book.sheets[1]  # 选定位置是1的工作表
#         sheet.pictures.add(fig1, top=0, left=0)
#         book.save("result_{}.xlsx".format(today))
#         book.close()
#         app.quit()
#         # 关闭python和sql之间的链接
#         conn.close()
#         print("图形插入成功")
#
#         # 发送邮件
#         # 1定义变量接收 邮箱服务器地址、端口、发件人账号、密码、收件人账号和邮件标题及邮件内容
#         host_ = "smtp.qq.com"  # 服务器地址
#         port_ = 465  # 端口号
#         user_ = '1071255432@qq.com'  # 发件人账号
#         password_ = 'ebskndibyzbrbbfb'  # 发件账号密码（授权码）
#         receivers_ = ['fzh006591@hotmail.com', 'fzh006591@sohu.com']  # 收件人账号列表
#         title_ = "账龄日报"  # 邮件标题
#         text_ = """Dear All:
#                                     附件是今天的账龄日报，请查收，有任何问题请联系我。
#                                     这是pycharm发送的test邮件
#                                     """  # 邮件正文
#         # 2发送邮件，需要指定邮件正文，通过MIMEMultipart函数
#         message = MIMEMultipart()  # 生成带有附件的邮件正文对象
#         message["Subject"] = Header(title_, charset="utf-8")  # 添加邮件的主题到邮件正文对象中
#         message["From"] = user_  # 添加发件邮箱到邮件对象
#         message["To"] = ";".join(receivers_)  # #添加收件邮箱到邮件对象
#         message.attach(MIMEText(text_, _subtype='plain', _charset="utf-8"))  # 带有带附件的正文内容
#         # 构造附件
#         att1 = MIMEText(open("result_{}.xlsx".format(today), 'rb').read(), "base64", 'utf-8')  # rb表示以二进制的形式读取数据
#         att1["Content-Type"] = 'application/octet-stream'  # 八位组流协议
#         att1["Content-Disposition"] = "attachment;filename=result_{}.xlsx".format(today)  # 附件
#         message.attach(att1)
#         # 发送邮件
#         smtp = smtplib.SMTP_SSL(host_)  # 指定服务器地址
#         smtp.connect(host_, port_)  # 链接到指定的服务器地址和端口号
#         smtp.login(user_, password_)  # 进行身份验证
#         smtp.sendmail(user_, receivers_, message.as_string())  # 参数包含发件人账号，收件人账号，邮件对象(数据类型要求字符串)
#         print("邮件发送成功")

# 1定义邮箱服务器地址、端口、发件人账号、密码、收件人账号和邮件标题及邮件内容
# from email.header import Header
# from email.mime.text import MIMEText
# import smtplib #SMTP协议客户端
# from  email.mime.multipart import MIMEMultipart
# host = 'smtp-mail.outlook.com'
# port = 25
# user = 'fzh006591@hotmail.com'
# password = 'fzh18301705292'
# receiver = ['10712554322@qq.com','fzh006591@sohu.com']
# title = 'pycharm邮件测式'
# text = 'python自动化发送，hotmail测试'
# # 2发送邮件，需要指定邮件正文，通过MIMEtext函数
# message = MIMEText(text,'plain','utf-8')
# #加入标题，及收件人
# message['Subject'] = Header(title,'utf-8')
# message['From'] = user
# message['To'] = ';'.join(receiver)
# #发送邮件
# smtp = smtplib.SMTP_SSL(host)
#
# smtp.connect(host,port)
# smtp.login(user,password)
# #发送，指定发件人账号，收件人账号，内容
# smtp.sendmail(user,receiver,message.as_string())


# # 1定义邮箱服务器地址、端口、发件人账号、密码、收件人账号和邮件标题及邮件内容
# host = 'smtp.qq.com'
# port = 465
# user = '1071255432@qq.com'
# password = 'ebskndibyzbrbbfb'
# receiver = ['fzh006591@hotmail.com','fzh006591@sohu.com']
# title = 'pycharm邮件测式'
# text = 'python自动化发送，无需回复'
# # 2发送邮件，需要指定邮件正文，通过MIMEtext函数
# message = MIMEText(text,'plain','utf-8')
# #加入标题，及收件人
# message['Subject'] = Header(title,'utf-8')
# message['From'] = user
# message['To'] = ';'.join(receiver)
# #发送邮件
# smtp = smtplib.SMTP_SSL(host)
# smtp.connect(host,port)
# smtp.login(user,password)
# #发送，指定发件人账号，收件人账号，内容
# smtp.sendmail(user,receiver,message.as_string())


# # 封闭函数
# def auto_picture(io_from, name, io_to, col):
#     '''
#     函数功能：汇总多个工作簿，并绘制拆线图
#     输出：含有拆线图的工作簿
#     io_from ：目标文件夹的地址
#     name:表中的列名，按哪个分组操作
#     io_to:导出工作薄的名称
#     col:
#
#
#     '''
#     import pandas as pd
#     import os
#     import matplotlib.pyplot as plt
#     import xlwings as xw
#
#     # 设置绘图风格
#     plt.style.use('seaborn')
#     # 设置字体为黑色
#     plt.rcParams['font.family'] = 'SimHei'
#     # 显示符号
#     plt.rcParams['axes.unicode_minus'] = False
#
#     df = pd.DataFrame()
#     for i in os.listdir(r'{}'.format(io_from)):
#
#         if i.startswith('~$'):
#             continue
#         data = pd.read_excel(r"{}\{}".format(io_from, i))
#         #         df1 = data.groupby('产品名称').agg({name:sum})
#         df1 = data.groupby(name).agg({col: sum})
#         df1.columns = [i.split('.')[0]]
#         df = pd.concat([df, df1], axis=1)
#     df.to_excel("半年{}.xlsx".format(io_to))
#     fig = plt.figure(figsize=(8, 5))
#     for i in df.index:
#         plt.plot(df.columns, df.loc[i], marker='v')
#     plt.title('产品半年统计表_{}'.format(io_to))
#     plt.xlabel('月份')
#     plt.ylabel(col)
#     plt.legend(df.index)
#
#     # 把图形插入到表格中
#
#     app = xw.App(visible=False, add_book=False)
#     book = app.books.open("半年{}.xlsx".format(io_to))
#     sheet = book.sheets[0]
#     # 插入图片，需要指定位置，left ,top
#     sheet.pictures.add(fig, left=0, top=89)
#     book.save()
#     book.close()
#     app.quit()
# auto_picture("C:\Data\Jupyter_file\Python数据清洗基础\办公自动化\汇总多个工作簿数据\销售统计",
#             '产品名称','利润表_4','销售利润（元）')
# from  requests_html import HTMLSession
# import pandas as pd
# s = HTMLSession()
# url = 'https://sz.lianjia.com/zufang/futianqu/pg1rt200600000001l1/#contentList'
#
# response = s.get(url)
# print(response.status_code)
# price = response.html.xpath('//em/text()')[:-2]
# print(price)
# s_price = pd.Series(price)
# price(s_price)
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
#
# from pyecharts.charts import Bar
# import seaborn as sns

# sns.set_theme(style="whitegrid")
#
# # Load the example planets dataset
# planets = sns.load_dataset("planets")
#
# cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
# g = sns.relplot(
#     data=planets,
#     x="distance", y="orbital_period",
#     hue="year", size="mass",
#     palette=cmap, sizes=(10, 200),
# )
# g.set(xscale="log", yscale="log")
# g.ax.xaxis.grid(True, "minor", linewidth=.25)
# g.ax.yaxis.grid(True, "minor", linewidth=.25)
# g.despine(left=True, bottom=True)
# bar = Bar()
# bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# bar.add_yaxis("商家B", [7, 10, 46, 20, 65, 95])
# # bar.render_notebook()
# # bar.show_config()
# bar.render('bar.html')
# # np.random.seed(1)
# data1 = {"x":["201{}".format(i) for i in range(10)],
#         "y":np.random.randint(2000,5000,10)}
# np.random.seed(2)
# data2 = {"x":["201{}".format(i) for i in range(10)],
#         "y":np.random.randint(2000,5000,10)}
# plt.plot(data1['x'],data1['y'])
# plt.figure()
# plt.plot(data1['x'],data1['y'])
# plt.show()
# se1 = pd.Series([1,3,3,4,5],index=list('abcde'),dtype='int32',name='age')
# print(type(se1))
# print(se1)
# arr = np.array([i for i in range(10)])
# print(arr)
# print(['{}*{}={}'.format(i,j,i*j) for i in range(1,10) for j in range(1,i+1)])
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%d '%(j,i,i*j),end='')
#     print()

# import pymysql
#
# con = pymysql.connect(host='127.0.0.1',user='root',password='1qaz@WSX',database='cda')
# cur = con.cursor()
# sql = 'select * from dept'
# result = cur.execute(sql)
# print(result)
# for i in cur.fetchall():
#     print(i)
# con.close()





# print(type(i for i in 'adfdfdfdafd'))
# print([i for i in 'afdfdfdfdf'])
# print((i for i in 'afdfd888fdfdf'))
# print(list(i for i in 'afdfdfdfdf'))



# def h():
#     print("你好")
#     yield 5
#     print("再见")
#     yield 6
#     yield 7
# g = h()
#
# print('----------------')
# for i in g:
#     print('111111111111111111111111')
#     print(i)
#     print('t',end='--')
#
# for i in g:
#     print('22222222222222222222222222')
#     print('ttst',end='==')
# print(g)
# print(list(g))









# print('abcd\\ef')
# print('abcd\bef')
# print('abcd\aef')
# print('abcd\vef')
# print('abcd\tef')
# print('abcd\ref')
# print('abcd'.split())


# print({i:j for i,j in enumerate('abcdef')})
# print(i for i in 'abcdefg')
# print(list(i for i in 'abcdef'))
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{} * {} = {}'.format(i,j,i*j),end='  ')
#     print()
# print(1,2,3,end='\t')
# print(4,5,6,end='\n')
# print('asdfg\nss', end='\n')
# print('hello,world')






# def g():
#     a = 1
#     while True:
#         yield a
#         a += 1
# a = g()
# print(next(g()))
# print(next(g()))
# print(next(g()))
# print(next(a),next(a),next(a))
# print(next(g()),next(g()),next(g()),next(g()))




# print([lambda x:x*i for i in range(10)])
# print([i for i in range(5)])
# print({i for i in range(5)})
# fun_1 = [lambda x:i for i in range(5)]
# print(fun_1)
# print(fun_1)
# prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
# print({key:prices[key] for key in prices if prices[key] > 100})
# for key,value in prices.items():
#     print(key,value)






# print({i:x for x,i in enumerate('12345')})
# print({i for i in enumerate('10')})
# generator_demo1 = (x*x for x in range(5))
# print(generator_demo1)
# print(list(generator_demo1))
#
# print(type([i for i in range(10)]))
# print(type(x for x in range(6)))
# print(type((x for x in range(6))))

# from bs4 import *
# def add(x,y):
#     return x+y
# print(add(1,2))
# import sum_
# print(sum_.sum_(1,2,3))
#
#
# tup = (1,2,3,4,5,6)
# a,b,c,d,e,f = tup
# print(a,b)














# import tkinter as tk
# class GameOjbect(object):
#     def __init__(self,canvas,item):
#         self.canvas = canvas
#         self.item= item
#     #删除方法
#     def delete(self):
#         self.canvas.delete(self.item)
#     #得到对象的坐标
#     def get_coords(self):
#         return self.canvas.coords(self.item)
#     #对象移动
#     def move(self,x,y):
#         self.canvas.move(self.item,x,y)
#
#
# class Racket(GameOjbect):
#     def __init__(self,canvas,x,y):
#         item = canvas.create_rectangle(x,y,x+90,y+10,fill= 'green')
#         super().__init__(canvas,item)
#
#     def draw(self,offset):
#         pos = self.get_coords()
#         width = self.canvas.winfo_width()
#         #当弹板在画布内时，按给定偏移量移动
#         if pos[0]+offset >= 0 and pos[2]+offset <= width:
#             super().move(offset,0)
#
# class Ball(GameOjbect):
#     def __init__(self,canvas,x,y):
#         self.direction = [1,-1]
#         self.speed = 10
#         item = canvas.create_oval(x,y,x+20,y+20,fill = 'blue')
#         super().__init__(canvas,item)
#
#     #绘制弹球
#     def draw(self):
#         pos = self.get_coords()
#         self.canvas_width= self.canvas.winfo_width()
#         #方向判断
#         if pos[1] <= 0:
#             self.direction[1] *= -1
#         if game.hit_racket():
#             self.direction[1] *= -1
#         if pos[0] <= 0 and pos[2] >= self.canvas_width:
#             self.direction[0] *= -1
#         #偏移量
#         x = self.direction[0] * self.speed
#         y = self.direction[1] * self.speed
#         self.move(x,y)
#
# #游戏类,定义完整过程
# class Game(tk.Frame):
#     def __init__(self,master):
#         super().__init__(master)
#         self.lives = 3
#         self.scores = 0
#         self.width = 800
#         self.height = 600
#         #设置画版放置
#         self.canvas = tk.Canvas(self,bg='#f8c26c',width=self.width,height= self.height)
#         self.canvas.pack()
#         self.pack()
#         self.ball = None
#         self.lives_text = None
#         self.scores_text = None
#         #初始化弹版
#         self.racket = Racket(self.canvas,self.width/2-45,480)
#         self.setup_game()
#         #将键盘焦点转移到画布组件上
#         self.canvas.focus_set()
#         #将键盘左右键与弹版左右移动函数绑定在一起
#         self.canvas.bind('<KeyPress-Left>',lambda turn_left:self.racket.draw(-20))
#         self.canvas.bind('<KeyPress-Right>',lambda turn_right:self.racket.draw(20))
#     #加载游戏
#     def setup_game(self):
#         #将球设置在弹板中间的位置的上方
#         self.reset_ball()
#         self.update_lives_text()
#         self.update_scores_text()
#         self.text = self.canvas.create_text(400,200,text='单击左键开始游戏',font=('Helvetica',36))
#         self.canvas.bind('<Button-1>',lambda start_game:self.start_game())
#     #在游戏预置时添加弹球，弹球在弹板中间位置上方
#     def reset_ball(self):
#         if self.ball != None:
#             self.ball.delete()
#         racket_pos = self.racket.get_coords()
#         x = (racket_pos[0]+racket_pos[2]) * 0.5-10
#         self.ball = Ball(self.canvas,x,350)
#
#     #更新生命的数字
#     def update_lives_text(self):
#         text = '生命:%s'% self.lives
#         if self.lives_text is None:
#             self.lives_text = self.canvas.create_text(60,30,text = text,
#                                                       font = ('Helvetica',16),fill= 'green')
#         else:
#             self.canvas.itemconfig(self.lives_text,text=text)
#     #更新得分数字
#     def update_scores_text(self):
#         text = '得分:%s'% self.scores
#         if self.scores_text is None:
#             self.scores_text = self.canvas.create_text(60, 60, text=text,
#                                                       font=('Helvetica', 16), fill='green')
#         else:
#             self.scores = self.scores +1
#             text = '得分:%s'% self.scores
#             self.canvas.itemconfig(self.scores_text, text=text)
#     #开始游戏
#     def start_game(self):
#        self.canvas.unbind('<Button-1>')
#        self.reset_score()
#        self.canvas.delete(self.text)
#        self.game_loop()
#
#     #重置得分为零
#     def reset_score(self):
#         self.scores = 0
#         text =  '得分:%s'% self.scores
#         self.canvas.itemconfig(self.scores_text, text=text)
#     #游戏循环
#     def game_loop(self):
#         if self.ball.get_coords()[3] >= self.height:
#             self.ball.speed = 0
#             self.lives -= 1
#             #小于零 ,游戏结束
#             if self.lives < 0:
#                 self.canvas.create_text(400,200,text='游戏结束',
#                 font = ('Helvetica',36),fill='red')
#             else:
#                 self.scores = self.scores -1
#                 self.after(1000,self.setup_game)
#         else:
#             self.ball.draw()
#             self.after(50,self.game_loop())
#
#     #每碰撞一次，更新一次得分
#     def hit_racket(self):
#         ball_pos = self.ball.get_coords()
#         racket_pos = self.racket.get_coords()
#         if ball_pos[2] >= racket_pos[0] and ball_pos[0] <= racket_pos[2]:
#             if ball_pos[3] >= racket_pos[1] and ball_pos[3] <= racket_pos[3]:
#                 self.update_scores_text()
#                 return True
#         return False
#
# if __name__=='__main__':
#     root = tk.Tk()
#     root.title('弹球游戏')
#     #窗口大小不可改变
#     root.resizable(0,0)
#     #窗口总是显示在最前面
#     root.wm_attributes("-topmost",1)
#     game = Game(root)
#     game.mainloop()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # import random
# # ran = random.randint(1,100)
# # print(ran)
# # # cho = random.choice([1,3,2,2,5,5])
# # # print(cho)
# # # while True:
# # #     throw_1 = random.randint(1,6)
# # #     throw_2 = random.randint(1,6)
# # #     total = throw_1+throw_2
# # #     print(total)
# # #     if throw_2 == 6 and  throw_1 ==6:
# # #         break
# # # print('两个六')
# #
# # ls = [1,3,2,2,5,5]
# # print(ls[1:3])
# # print(ls+ls)
# # ls.sort()
# # print(ls)
# # print(ls[-6])
# # def get_guess(word):
# #     return 'a'
# #
# # def process_guess(guess,work):
# #     global lives_remaining
# #     lives_remaining = lives_remaining - 1
# #     return False
# #
# # x = 'abc'.center(10,'-')
# # print(x)
# # x2 = x.splitlines()
# # print(x2)
# # y = ['1','2','3']
# # # y2 = int(y)
# # print(y)
# # # print(y2)
# # import lianjia
# # print(lianjia.result)
# # import pygame
# # print(type('abc'))
# # cc = str(3333)
# import requests
# import urllib.request
# # url = 'https://pic.rmb.bdstatic.com/bjh/down/336fadf70477f381057be1fe137cf938.jpeg'
# # con = requests.get(url)
# # con.encoding = 'utf8'
# # print(con.text)
# # urllib.request.urlretrieve(url,'pic.jpg')
# from    PIL import Image
# import pytesseract
# import re
# import os
# # image = Image.open(r'pic.jpg')
# # text = pytesseract.image_to_string(Image,lang='chi_sim')
# # file = open('./imag_test.txt',mode='w')
# # file.writelines(text)
# # file.close()
#
# # file = './pic.jpg'
# # image = Image.open(file)
# # result = pytesseract.image_to_string(image,lang='chi_sim')
#
#
#
# # from cnocr import CnOcr
# # file = './pic.jpg'
# # ocr = CnOcr()
# # result = ocr.ocr(file)
# # print(f'Predicted Chars:{result}')
