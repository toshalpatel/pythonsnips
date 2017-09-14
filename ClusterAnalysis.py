# CLUSTER ANALYSIS 

# Set the working directory 

# Import the required libraries 
from sklearn import cluster
import pandas as pd
from pandas import DataFrame

# Load the data into a dataset 
retail = pd.read_csv ("Shoppers.csv")
retail.info()

# Construct the predictor vector, and scale the input data 
X = array (retail [['MOB', 'MaxBalanceAmt', 'CntPurchActMth', 'TotFinCharge', 'PctOnlineTrans', 'PctPromoSale', 'PayToBalRatio', 'PctOfflinePymt', 'CntActiveCards']])
mu = X.mean (axis=0)
sigma = X.std (axis=0)
Xs = (X - mu) / sigma

# Iterate the clustering exercise over various numbers of clusters in the solution 
n_clusters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
cluster_labels = ['Cluster-1', 'Cluster-2', 'Cluster-3', 'Cluster-4', 'Cluster-5', 'Cluster-6', 'Cluster-7', 'Cluster-8', 'Cluster-9', 'Cluster-10', 'Cluster-11', 'Cluster-12']
cluster_sols = ['1-Cluster sol', '2-Cluster sol', '3-Cluster sol', '4-Cluster sol', '5-Cluster sol', '6-Cluster sol', '7-Cluster sol', '8-Cluster sol', '9-Cluster sol', '10-Cluster sol', '11-Cluster sol', '12-Cluster sol']
inertia = zeros (12)
size = zeros ((12,12))
for i in arange(12):
	algorithm = cluster.KMeans(n_clusters=n_clusters[i], init='k-means++')
	model = algorithm.fit (Xs)
	labels = algorithm.labels_
	cluster_count = len (unique (labels))
	print 'K-Means -  # Clusters:', cluster_count
	centroids = algorithm.cluster_centers_
	ClusterCenters = (centroids * sigma) + mu
	ClusterCenters = ClusterCenters.T
	ClusterProfiles = DataFrame()
	ClusterProfiles ['Features'] = array (('MOB', 'MaxBalanceAmt', 'CntPurchActMth', 'TotFinCharge', 'PctOnlineTrans', 'PctPromoSale', 'PayToBalRatio', 'PctOfflinePymt', 'CntActiveCards'))
	for j in arange(cluster_count):
		ClusterProfiles [cluster_labels[j]] = ClusterCenters [:,j]
	print ClusterProfiles
	inertia[i] = algorithm.inertia_
	for k in unique (labels):
		is_class_member = (labels==k)
		class_sample = X [is_class_member]
		size [i,k] = len (class_sample)

# Explore the sizes of the various clusters, for each iteration conducted above 
ClusterSizes = DataFrame()
ClusterSizes ['Solution'] = cluster_sols
for p in arange(12):
	ClusterSizes [cluster_labels[p]] = size [:,p] / len(Xs) * 100
print 'Cluster sizes:'
print ClusterSizes

# Construct the Scree Plot 
fig = plt.figure()
ax = fig.add_subplot (1,1,1)
for i in arange(12):
	ax.scatter (i+1, inertia[i] / inertia[0] * 100)
ax.set_xlabel ('Number of Clusters')
ax.set_ylabel ('% Within Cluster Variation')
ax.set_title ('Scree Plot')

# Build a cluster solution with six clusters 
size = zeros (6)
cluster_labels = ['Cluster-1', 'Cluster-2', 'Cluster-3', 'Cluster-4', 'Cluster-5', 'Cluster-6']
algorithm = cluster.KMeans(n_clusters=6, init='k-means++')
model = algorithm.fit (Xs)
labels = algorithm.labels_
cluster_count = len (unique (labels))
print 'K-Means -  # Clusters:', cluster_count
centroids = algorithm.cluster_centers_
ClusterCenters = (centroids * sigma) + mu
ClusterCenters = ClusterCenters.T
ClusterProfiles = DataFrame()
ClusterProfiles ['Features'] = array (('MOB', 'MaxBalanceAmt', 'CntPurchActMth', 'TotFinCharge', 'PctOnlineTrans', 'PctPromoSale', 'PayToBalRatio', 'PctOfflinePymt', 'CntActiveCards'))
for j in arange(cluster_count):
	ClusterProfiles [cluster_labels[j]] = ClusterCenters [:,j]
print ClusterProfiles
