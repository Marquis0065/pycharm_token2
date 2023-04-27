# @Time: 2023/2/16 14:04
# _*_coding : utf-8 _*_
# @Authon : 
# @File : 机器学习
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fa_kit import FactorAnalysis
from sklearn.decomposition import PCA
import warnings
warnings.filterwarnings("ignore")
import os
os.chdir(r"C:\Data\Jupyter_file\机器学习")

df = pd.read_csv('profile_bank')
print(df.head())
# pca = PCA(n_components=3)
# pca.fit(model_)


