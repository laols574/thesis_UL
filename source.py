import csv

filename = input("File Name: ")

with open(filename, newline='') as csvfile:
                corpus = list(csv.reader(csvfile))
comment = 3
source = 0
reply_to = 1

new = []

for f in corpus:
	reply = f[reply_to]
	s = 0 
	for i in corpus:
		if(reply == i[source]):
			s = i[comment]
	if(s != 0):
		new.append([f[comment], s])

corpus = new		

len_f = len(filename) - 4
out_file = filename[0:len_f] 

file = open("mout.csv", "w+")
file.write("comment,source\n")
for line in corpus:
	file.write('"' + line[0] + '","' + line[1] + '"\n')

file.close()

