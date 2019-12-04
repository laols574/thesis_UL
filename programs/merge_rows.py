import csv

filename = "hpc_final_form.csv"

with open(filename, newline='') as csvfile:
                corpus = list(csv.reader(csvfile))

#each key will be a list holding the values 
url = 6

source = 0
reply_to = 1
date = 2
text = 4
reactions = 3
likes = 5
url = 6
ahah = 7
love = 8
wow = 9
sigh = 10
grrr = 11
name = 12
gender = 13
birthday = 14
current_city = 15
hometown = 16
work = 17
education = 18
interested_in = 19

#corpus_r = corpus.reverse()

names = [row[0] for row in corpus]
print(names[0:20])

for row in corpus:
	t = row[text].split()
	if(len(t) > 1):
		p_name = t[0] + " " + t[1]
		
		if(p_name in names):
			row[reply_to] = p_name 
	
f = ['source','reply_to','date','text', \
                               'reactions','likes','url', 'ahah','love','wow', \
                               'sigh','grrr','name', \
                               'gender', 'birthday', 'current_city',\
                               'hometown', 'work', 'education', 'interested_in']

f2 = ["source", "reply_to", "date", "reactions", "text"]
corpus.insert(0, f2)

with open("trump_comments_replies_update.csv", 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(corpus)
