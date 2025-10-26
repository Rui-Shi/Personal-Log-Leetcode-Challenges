import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

def k_means_by_label(X, k, max_iters=100):
    """
    使用“簇标签不再变化”作为停止条件的K-Means算法。
    """
    # 1. 初始化
    n_samples, n_features = X.shape
    random_indices = np.random.choice(n_samples, k, replace=False)
    centroids = X[random_indices]
    
    # 初始化簇标签数组
    clusters = np.zeros(n_samples)

    for i in range(max_iters):
        # 存储旧的簇标签，用于判断是否收敛
        old_clusters = clusters.copy()
        
        # 2. 分配 (Assignment)
        for idx, sample in enumerate(X):
            distances = [np.sqrt(np.sum((sample - point)**2)) for point in centroids]
            cluster_idx = np.argmin(distances)
            clusters[idx] = cluster_idx

        # 【新的停止条件】
        # 判断新旧簇标签数组是否完全相同
        if np.array_equal(old_clusters, clusters):
            print(f"算法在第 {i+1} 次迭代后收敛 (基于标签)。")
            break

        # 3. 更新 (Update)
        for cluster_idx in range(k):
            points_in_cluster = X[clusters == cluster_idx]
            if len(points_in_cluster) > 0:
                centroids[cluster_idx] = np.mean(points_in_cluster, axis=0)
            
    return centroids, clusters

# --- 运行和测试 ---
if __name__ == '__main__':
    X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.8, random_state=0)
    k = 4
    
    final_centroids, final_clusters = k_means_by_label(X, k)
    
    # 可视化结果 (代码同前)
    plt.scatter(X[:, 0], X[:, 1], c=final_clusters, s=50, cmap='viridis')
    plt.scatter(final_centroids[:, 0], final_centroids[:, 1], c='red', s=200, marker='*', edgecolor='black', label='Centroids')
    plt.title(f"K-Means Clustering (Stopped by Labels)")
    plt.legend()
    plt.show()

class ML_clustering:
    def __init__(self, input_data):
        self.data = input_data
    
    def k_means(self, k: int, max_iters = 5000) -> list:
        n_samples, _ = self.data.shape
        random_indices = np.random.choice(n_samples, k, replace=False)
        centroids = self.data[random_indices]
        clusters = np.zeros(n_samples)
        
        for _ in range(max_iters):
            old_clusters = clusters.copy()
            for index, point in enumerate(self.data):
                distances = [np.sqrt(np.sum((point - centroid)**2)) for centroid in centroids]
                clusters[index] = np.argmin(distances) # gives you the index of the min
            
            if np.array_equal(old_clusters, clusters):
                break
            
            for cluster_index in range(k):
                points_in_cluster = self.data[clusters == cluster_index]
                if len(points_in_cluster) > 0:
                    centroids[cluster_index] = np.mean(points_in_cluster, axis=0)
    
        return centroids, clusters


class K_means:
    def __init__(self, input_data, k, max_iter):
        self.input_data = input_data
        self.k = k
        self.max_iter = max_iter
    
    def fit(self):
        n, d = self.input_data.shape
        random_index = np.random.choice(n, k, replace = False)
        centroids = self.input_data[random_index]
        cluster_labels = np.zero(n)
        
        for _ in range(self.max_iter):
            old_cluster_labels = cluster_labels.copy()
            for index, point in enumerate(self.input_data):
                dists = [np.sqrt(np.sum((point - centroid) ** 2)) for centroid in centroids]
                cluster_labels[index] = np.argmin(dists)
            
            if old_cluster_labels == cluster_labels:
                break
            
            for cluster_index in range(k):
                clusters = self.input_data[cluster_labels == cluster_index]
                centroids[cluster_index] = np.mean(clusters, axis = 0)
        
        return centroids, cluster_labels
                
        
                    
            
        
            


        
        
