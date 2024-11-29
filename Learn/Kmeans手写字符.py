import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn import metrics
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

# 加载手写字符数据集
digits = datasets.load_digits()
data = digits.data
target = digits.target

# 使用Kmeans算法对数据进行聚类
kmeans = KMeans(n_clusters=10, random_state=0)
clusters = kmeans.fit_predict(data)

# 评估聚类结果的准确性
accuracy = metrics.adjusted_rand_score(target, clusters)
print("Adjusted Rand Index:", accuracy)

# 可视化聚类结果
fig, ax = plt.subplots(2, 5, figsize=(8, 3))
centers = kmeans.cluster_centers_.reshape(10, 8, 8)
for axi, center in zip(ax.flat, centers):
    axi.set(xticks=[], yticks=[])
    axi.imshow(center, interpolation='nearest', cmap=plt.cm.binary)

plt.show()
