'''
Lauren Olson
'''

import csv

with open('trump_comments_r_p.csv', newline='') as csvfile:
    file_array = list(csv.reader(csvfile))

source = 0
reply_to = 1
date = 2
text = 3
reactions = 4
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

likes_c = 0
ahah_c = 0
love_c = 0
wow_c = 0
sigh_c = 0
grrr_c = 0
name_c = 0
gender_c = 0
birthday_c = 0
current_c = 0
hometown_c = 0
work_c = 0
education_c = 0
interest_c = 0

all_text = "" 

for row in file_array:
  if(row[likes] != ""):
    likes_c += 1
  if(row[ahah] != ""):
    ahah_c += 1
  if(row[love] != ""):
    love_c += 1
  if(row[wow] != ""):
    wow_c += 1
  if(row[sigh] != ""):
    sigh_c += 1
  if(row[grrr] != ""):
    grrr_c += 1
  if(row[name] != ""):
    name_c += 1
  if(row[gender] != ""):
    gender_c += 1
  if(row[birthday] != ""):
    birthday_c += 1
  if(row[current_city] != ""):
    current_c += 1
  if(row[hometown] != ""):
    hometown_c += 1
  if(row[work] != ""):
    work_c += 1
  if(row[education] != ""):
    education_c += 1
  if(row[interested_in] != ""):
    interest_c += 1
    

output_data = ""
output_data += "Likes: " + str(likes_c) + "\n"
output_data += "Ahah: " + str(ahah_c) + "\n"
output_data += "Love: " + str(love_c) + "\n"
output_data += "Wow: " + str(wow_c) + "\n"
output_data += "Sigh: " + str(sigh_c) + "\n"
output_data += "Grrr: " + str(grrr_c) + "\n"
output_data += "Name: " + str(name_c) + "\n"
output_data += "Gender: " + str(gender_c) + "\n"
output_data += "Birthday: " + str(birthday_c) + "\n"
output_data += "Current City: " + str(current_c) + "\n"
output_data += "Hometown: " + str(hometown_c) + "\n"
output_data += "Work: " + str(work_c) + "\n"
output_data += "Education: " + str(education_c) + "\n"
output_data += "Interested In: " + str(interest_c) + "\n"

output_file = open("r_p_count.txt", "w+")
output_file.write(output_data)

#file.close()
output_file.close()
