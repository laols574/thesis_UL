import numpy
import pandas
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import matplotlib.pyplot as plt
from scipy.sparse import *
import matplotlib.colors
from nltk.corpus import stopwords 

'''
Lauren Olson
This is a file which clusters raw text data 
'''

def main():
	file = open("mergedcorpus_u.txt", "r+")
	corpus = file.readlines()
	cluster(corpus, 5)

def cluster(corpus, k):
	eng = list(set(stopwords.words('english')))

	trump = ['wall', 'president', 'trump', 'loss', 'yes', 'sorry', 'mr', 'build', 'thank', 'people']

	s_w = eng + trump

	vectorizer = TfidfVectorizer(stop_words=s_w, ngram_range=(2,2))
	x = vectorizer.fit_transform(corpus)
	
	x = coo_matrix(x).tocsr()

	model = KMeans(n_clusters=k)
	model.fit(x)

	order_clusters = model.cluster_centers_.argsort()[:, ::-1]
	terms = vectorizer.get_feature_names()
	
	x = x.todense()


	centers = model.cluster_centers_

	print("top terms per cluster:")

	for i in range(k):
		print("Cluster: " , i)
		for ind in order_clusters[i, :10]:
			print(terms[ind]) 



"""
create functionality for clustering 
"""


if __name__=="__main__":
	main()
