import string
import re

file = open("output.txt", "r+")

file_array = file.readlines()

l = ["immigrant", "immigrants"]

slur_count = 0

slur_dict = {}
slur2txt = {}

new_arr = []

for row in file_array:
	a = row.split()
	a = [word.strip().lower() for word in a]
	
	a = [re.sub(r'[^\w\s]','',word) for word in a]
	for word in a:
		if( word not in slur2txt.keys()):
			slur2txt[word] = [row]
		else:
			slur2txt[word] = slur2txt[word] + [row]
 
	new_arr += a

set_of_comments = set()
illegal = 0
for word in new_arr:
	row = slur2txt[word]
	
	if("illegal" in str(row).split() or "illegals" in str(row).split()):
		illegal += 1
		print(row)
		break

	if(word in l):
		slur_count += 1	
		if(word not in slur_dict.keys()):
			slur_dict[word] = 1
			set_of_comments.add(tuple(row))
		else:
			slur_dict[word] = slur_dict[word] + 1
			set_of_comments.add(tuple(row))
			
print(illegal)
file = open("immigrant_count-illegal", "w+")

for entry in slur_dict:
	file.write(str(entry) +  ": " + str(slur_dict[entry]) + "\n")

file.write("comments with slurs: \n")
for list in set_of_comments:
	for comment in list:
		file.write(str(comment) + "\n")

file.write("total: " + str(slur_count))
file.close()
