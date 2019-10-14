'''
Lauren Olson
'''

import csv

with open('trump_comments_r_p.csv', newline='') as csvfile:
    file_array = list(csv.reader(csvfile))


all_text = ""
i= 1 
for row in file_array:
  print(i, " ", len(row))
  i += 1  
  ''' if(row[0] == "Apple Rivera"):
    for i in row:
      all_text += i + "\n"
    all_text += "\n\n\n\n"'''


output_file = open("mariacheck.txt", "w+")
output_file.write(all_text)

file.close()
output_file.close()
