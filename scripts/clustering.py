from sklearn.cluster import KMeans
import pandas as pd

def clusterize(data, column, n_clusters):
    '''Clusters the specified column.'''
    feature = data[[column]]
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    data[f'{column}_cluster'] = kmeans.fit_predict(feature)
    return kmeans, data