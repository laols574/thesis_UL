import numpy
import pandas
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import matplotlib.pyplot as plt
from scipy.sparse import *
import matplotlib.colors
from nltk.corpus import stopwords 
from afinn import Afinn

'''
Lauren Olson
This is a file which clusters raw text data 
'''

def main():
	file = open("output.txt", "r+")
	corpus = file.readlines()
	af = Afinn()

	text2score = {}
	text2sentiment = {}
	
	for comment in corpus:
		text2score[comment] = af.score(comment)

	pos = 0
	neg = 0
	neutral = 0
	for comment in text2score:
		score = text2score[comment]
		if(score > 0):
			text2sentiment[comment] = 'positive'
			pos += 1
		if(score < 0):
			text2sentiment[comment] = 'negative'
			neg += 1
		else:
			text2sentiment[comment] = 'neutral'
			neutral += 1

	file = open("sent_out.txt", "w+")
	
	file.write("Positive: " + str(pos) + "\n")
	file.write("Negative: " + str(neg) + "\n")
	file.write("Neutral: " + str(neutral) + "\n")

	for comment in text2sentiment:
		out = str(text2sentiment[comment]) +  ": " + str(comment) + "\n"
		file.write(out)	

	file.close()

"""
create functionality for clustering 
"""


if __name__=="__main__":
	main()
