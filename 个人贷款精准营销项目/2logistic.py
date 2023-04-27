# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 17:54:19 2021

@author: Lenovo
"""



# In[1]:

import os
import numpy as np
from scipy import stats
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

#pd.set_option('display.max_columns', None)
#os.chdir(r"D:\Python_book\8Logistic")

# 导入数据和数据清洗

# In[5]:

accepts = pd.read_csv(r'd:\testana2.csv')
#%%

# In[10]:

train = accepts.sample(frac=0.7, random_state=1234).copy()
test = accepts[~ accepts.index.isin(train.index)].copy()
print(' 训练集样本量: %i \n 测试集样本量: %i' %(len(train), len(test)))


# In[11]:

lg = smf.glm('y ~ C(Sex)+GDP+A4+A10+A11+A12+A13+A14+A15+a16+age+avg_balance+cv_balance', data=train, 
             family=sm.families.Binomial(sm.families.links.logit)).fit()
lg.summary()

#%%
# 向前法
def forward_select(data, response):
    import statsmodels.api as sm
    import statsmodels.formula.api as smf
    remaining = set(data.columns)
    remaining.remove(response)
    selected = []
    current_score, best_new_score = float('inf'), float('inf')
    while remaining:
        aic_with_candidates=[]
        for candidate in remaining:
            formula = "{} ~ {}".format(
                response,' + '.join(selected + [candidate]))
            aic = smf.glm(
                formula=formula, data=data, 
                family=sm.families.Binomial(sm.families.links.logit)
            ).fit().aic
            aic_with_candidates.append((aic, candidate))
        aic_with_candidates.sort(reverse=True)
        best_new_score, best_candidate=aic_with_candidates.pop()
        if current_score > best_new_score: 
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_new_score
            print ('aic is {},continuing!'.format(current_score))
        else:        
            print ('forward selection over!')
            break
            
    formula = "{} ~ {} ".format(response,' + '.join(selected))
    print('final formula is {}'.format(formula))
    model = smf.glm(
        formula=formula, data=data, 
        family=sm.families.Binomial(sm.families.links.logit)
    ).fit()
    return(model)


# In[23]:
#%%

candidates = ['y', 'GDP','A4','A10','A11','A12','A13','A14','A15','a16','age','avg_balance','cv_balance']
data_for_select = train[candidates]

lg_m1 = forward_select(data=data_for_select, response='y')
lg_m1.summary().tables[1]
#%%
lg = smf.glm('y ~ cv_balance + avg_balance + A10 + A4', data=train, 
             family=sm.families.Binomial(sm.families.links.logit)).fit()
lg.summary()
#%%
# 预测

# In[19]:

train['proba'] = lg.predict(train)
test['proba'] = lg.predict(test)

test['proba'].head(10)

# In[12]:
# ## 模型评估

# - 绘制ROC曲线

# In[27]:

import sklearn.metrics as metrics

fpr_test, tpr_test, th_test = metrics.roc_curve(test.y, test.proba)
fpr_train, tpr_train, th_train = metrics.roc_curve(train.y, train.proba)

plt.figure(figsize=[3, 3])
plt.plot(fpr_test, tpr_test, 'b--')
plt.plot(fpr_train, tpr_train, 'r-')
plt.title('ROC curve')
plt.show()


# In[28]:

print('AUC = %.4f' %metrics.auc(fpr_test, tpr_test))

