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

import csv

'''
Lauren Olson
This is a file which clusters raw text data 
'''

def main():
	'''with open('trump_comments_r_p.csv', newline='') as csvfile:
		corpus = list(csv.reader(csvfile))
	
	l = []
	for i in corpus:
		l.append(i[3])
	corpus = l'''
	
	file = open("mergedcorpus_u.txt")
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
		elif(score < 0):
			text2sentiment[comment] = 'negative'
			neg += 1
		else:
			text2sentiment[comment] = 'neutral'
			neutral += 1

	file = open("mc_sentiment.txt", "w+")
	file.write("Negative: " + str(neg)  + " Percent: " + str(100*(neg/(neutral+ pos + neg))))
	file.write("Positive: " + str(pos)  + " Percent: " + str(100*(pos/(neutral+ pos + neg))))
	file.write("Neutral: " + str(neutral) + " Percent: " + str(100*(neutral/(neutral+ pos + neg))))
	file.close()

	with open('mc_sentiment.csv', mode='w+') as output:
		sent_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		for comment in text2sentiment:
			sent_writer.writerow([str(text2sentiment[comment]), str(comment) ])

"""
create functionality for clustering 
"""


if __name__=="__main__":
	main()
