'''
Lauren Olson
'''


file = open("trump_comments2.csv", "r+")

file_array = file.readlines()

all_text = ""

for row in file_array:
  row = row.split(",")
  all_text += row[4] + "\n"

output_file = open("output.txt", "w+")
output_file.write(all_text)

file.close()
output_file.close()
