import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from sklearn.decomposition import PCA

# 加载鸢尾花卉数据集
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 使用PCA将数据降维到2维，便于可视化
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# 创建KMeans模型并进行训练
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_pca)

# 预测类别
predicted_labels = kmeans.labels_

# 可视化结果
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=predicted_labels, cmap='viridis')
plt.title('KMeans Clustering of Iris Dataset')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.show()

# 评估模型
ari = adjusted_rand_score(y, predicted_labels)
print(f"Adjusted Rand Index (ARI) 分数为: {ari}")
