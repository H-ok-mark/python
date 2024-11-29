import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree#导入决策树
from sklearn import metrics
import lightgbm as lgb
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

# 加载数据
# 假设你的数据文件名为 diabetes.csv，并且目标变量是 'target'
diabetes = load_diabetes()
data = pd.DataFrame(diabetes.data)
print(data.head())  # 输出前五行的data
target = pd.DataFrame(diabetes.target)
print(target.head())
data = diabetes['data']
target = diabetes['target']
feature_names = diabetes['feature_names']
df = pd.DataFrame(data, columns=(feature_names))
print("查看数据集的基本信息:", df.info())

train_X, test_X, train_y, test_y = train_test_split(data, target, test_size=0.2)
print(train_X.shape, train_y.shape)

model=tree.DecisionTreeClassifier()#加载决策树模型

model.fit(train_X,train_y)#训练模型

pre_y = model.predict(test_X)  # 预测

print("准确率:", metrics.accuracy_score(test_y, pre_y))  # 模型评估。

# criterion参数的调整，默认为gini指数
# 该参数对应的三个函数对应信息增益，增益率和基尼系数，每个函数对应的评价指标有所不同，有各自的特点。
# 将该参数进行更换为信息增益--entropy。
model2 = tree.DecisionTreeClassifier(criterion='entropy')
model2.fit(train_X, train_y)
pre_y = model2.predict(test_X)
print("criterion参数改为信息增益(entropy)的准确率:", metrics.accuracy_score(test_y, pre_y))

# max_depth最大深度的调整，默认为不限制最大深度
# 该参数为树的最大深度，当样本中的特征较多时，设置适当的最大深度可以防止模型过拟合。
# 尝试调整max_depth这个参数以达到模型更好的效果。

model3 = tree.DecisionTreeClassifier(max_depth=2)
model3.fit(train_X, train_y)
pre_y = model3.predict(test_X)
print("max_depth深度参数改为2的准确率:", metrics.accuracy_score(test_y, pre_y))
