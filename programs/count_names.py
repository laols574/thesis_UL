import csv

with open('trump_comments_r_p.csv', newline='') as csvfile:
                corpus = list(csv.reader(csvfile))

names = [c[0] for c in corpus]
print("len of names: ", len(names))

file = open("names_corpus.txt", "w+")
file.write(str(names) + "\n\n\n")

name_count = {}
for name in names:
	if(name in name_count):
		name_count[name] = name_count[name] + 1
	else:
		name_count[name] = 1

l = sorted(name_count.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)

file.write("amount of names: " + str(len(name_count)) + "\n\n\n")

for i in l:
	file.write("Name: " + str(i) + "\n")

num_dict = {}
for name in name_count:
	if(name_count[name] in num_dict):
		num_dict[name_count[name]] = num_dict[name_count[name]] + 1
	else:
		num_dict[name_count[name]] = 1

for entry in num_dict:
	file.write("Amount: " + str(entry) + " Occurence: " + str(num_dict[entry]) + "\n")

file.close()
