import numpy
import pandas
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import matplotlib.pyplot as plt
from scipy.sparse import *
import matplotlib.colors
from nltk.corpus import stopwords 
from sklearn.decomposition import PCA
	
'''
Lauren Olson
This is a file which clusters raw text data 
'''

def main():
	file = open("output.txt", "r+")
	corpus = file.readlines()
	cluster(corpus, 2)

def cluster(corpus, k):
	random_state = 0

	eng = list(set(stopwords.words('english')))

	trump = ['wall', 'president', 'trump', 'loss', 'yes', 'sorry', 'mr', 'build', 'thank', 'people']

	s_w = eng + trump

	vectorizer = TfidfVectorizer(stop_words=s_w)
	vectorizer.fit(corpus)
	features = vectorizer.transform(corpus)
	
	cls = KMeans(n_clusters=k)
	cls.fit(features)

	cls.predict(features)

	pca = PCA(n_components=2, random_state=random_state)
	reduced_features = pca.fit_transform(features.toarray())
	
	reduced_cluster_centers = pca.transform(cls.cluster_centers_)

	plt.scatter(reduced_features[:,0], reduced_features[:,1], c=cls.predict(features))
	plt.scatter(reduced_cluster_centers[:,0], reduced_cluster_centers[:,1], marker="x", s=150, c='b')
	
	plt.show()


"""
create functionality for clustering 
"""


if __name__=="__main__":
	main()
