import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn import metrics

# 加载数据集
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 数据预处理
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 使用PCA降维
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# 使用DBSCAN算法进行聚类
dbscan = DBSCAN(eps=0.5, min_samples=5)
clusters = dbscan.fit_predict(X_pca)

# 评估聚类算法的准确率
print("Adjusted Rand Index:", metrics.adjusted_rand_score(y, clusters))

# 可视化聚类结果
plt.figure(figsize=(10, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters, cmap='viridis')
plt.title('DBSCAN Clustering of Iris dataset')
plt.show()


