import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.decomposition import PCA

# 加载手写字符数据集
digits = datasets.load_digits()
data = digits.data
print(data.shape)

# 数据预处理
data = StandardScaler().fit_transform(data)

# 调用DBSCAN算法进行聚类
dbscan = DBSCAN(eps=4, min_samples=5)
clusters = dbscan.fit_predict(data)

# 输出评估结果
print('聚类数量:', len(np.unique(clusters)))
print('轮廓系数:', metrics.silhouette_score(data, clusters))

# 使用PCA将数据降维到2维
pca = PCA(n_components=2)
data_2d = pca.fit_transform(data)

# 可视化结果
plt.figure(figsize=(10, 6))
plt.scatter(data_2d[:, 0], data_2d[:, 1], c=clusters, cmap='viridis')
plt.title('DBSCAN Clustering of Handwritten Digits')
plt.show()


