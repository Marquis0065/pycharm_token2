import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fa_kit import FactorAnalysis
import warnings
warnings.filterwarnings("ignore")
plt.rcParams['font.sans-serif'] = ['Heiti TC']
plt.rcParams['font.family'] = ['Heiti TC']
plt.rcParams['axes.unicode_minus'] = False
import os
os.chdir("C:\Data\Jupyter_file\机器学习")
df=pd.read_csv("cities_11.csv")

#获取要用的特征
model_data=df.loc[:,"X1":]
#查看相关系数
model_data.corr()
#标准化
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaler_model_data=scaler.fit_transform(model_data)
#PCA
from sklearn.decomposition import PCA
pca=PCA(n_components=2)
pca.fit(scaler_model_data)
print("主成分的可解释的变异的比例\n",pca.explained_variance_ratio_)
#实例化 对输入数据进行主成分的提取
fa=FactorAnalysis.load_data_samples(
    scaler_model_data,
    preproc_demean=True,
    preproc_scale=True
)
fa.extract_components()
#设定提取主成分的方式 使用top_n
fa.find_comps_to_retain(method="top_n",num_keep=2)
#最大方差法对因子进行旋转
fa.rotate_components(method="varimax")
#因子的载荷矩阵
fa.comps["rot"]
#输出因子得分
fa_scores=fa.get_component_scores(scaler_model_data)
fa_scores=pd.DataFrame(fa_scores,columns=["Gross","Avg"])
print(fa_scores)
cities_fa_scores=df.join(fa_scores)

# 画图 先人眼看看这几类城市划分几个类
plt.rcParams['font.family'] = 'Heiti TC'  # 'SimHei' #'Heiti TC'
from pylab import mpl
from pylab import mpl

mpl.rcParams['axes.unicode_minus'] = False


def scatter(x, y, labels, **kw):
    plt.figure(figsize=(6, 4))
    plt.yticks(size=12)
    plt.xticks(size=12)
    plt.scatter(x, y)
    for xx, yy, label in zip(x, y, labels):
        plt.text(xx, yy, '%s.' % label,
                 ha='center', va='bottom', **kw)


plt.show()

#画图
x=cities_fa_scores["Gross"]
y=cities_fa_scores["Avg"]
labels=cities_fa_scores["AREA"]
scatter(x,y,labels)

#层次聚类
import scipy.cluster.hierarchy as sch

#计算点-点距离 生成欧式距离矩阵
dis_mat=sch.distance.pdist(cities_fa_scores[["Gross","Avg"]],metric="euclidean")

#计算类-类之间的距离
Z=sch.linkage(dis_mat,method="ward")

#将层次聚类结果层次聚类图
P=sch.dendrogram(Z,labels=cities_fa_scores["AREA"].tolist())
plt.savefig("我的层次聚类图.png")