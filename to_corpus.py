import csv

filename = input("File Name: ")

with open(filename, newline='') as csvfile:
                corpus = list(csv.reader(csvfile))
text = 3
corpus = [f[text] for f in corpus]
corpus = corpus[1:-1]

len_f = len(filename) - 4
out_file = filename[0:len_f] 
file = open(out_file, "w+")

for line in corpus:
	file.write(line + "\n")

file.close()
