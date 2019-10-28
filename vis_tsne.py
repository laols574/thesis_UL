import numpy
import pandas
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from scipy.sparse import *
import matplotlib.colors
from nltk.corpus import stopwords 
from sklearn.decomposition import PCA
from yellowbrick.text import TSNEVisualizer
from yellowbrick.datasets import load_hobbies
import csv
	
'''
Lauren Olson
This is a file which clusters raw text data 
'''

def main():
	with open('mc_sentiment.csv', newline='') as csvfile:
		corpus = list(csv.reader(csvfile))
	cluster(corpus, 2)

def cluster(corpus, k):
	y = [i[0] for i in corpus]
	corpus = [i[1] for i in corpus]
	eng = list(set(stopwords.words('english')))

	trump = ['wall', 'president', 'trump', 'loss', 'yes', 'sorry', 'mr', 'build', 'thank', 'people']

	s_w = eng + trump

	vectorizer = TfidfVectorizer(stop_words=s_w)
	vectorizer.fit(corpus)
	features = vectorizer.transform(corpus)
	
	
	tsne = TSNEVisualizer()
	tsne.fit(features, y)
	tsne.show()
"""
create functionality for clustering 
"""


if __name__=="__main__":
	main()
