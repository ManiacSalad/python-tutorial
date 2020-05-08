
# ['Spider-Man','Captain America','Thor','Iron Man']
# ['The Hulk','Black Panther','Doctor Strange']
# create 2 list
# name1 , name2 , name3
# concatenate all the iteams in name3
# add your name (append it)
# now we need non magical super hero's so you will remove  'Doctor Strange'
# 9 super hero's
#Power_points = {'Spider-Man': 70 , 'Captain America': 70 ,
#               'The Thor': 85,'Iron Man': 50,
#               'The Hulk':70,'Black Panther': 66,'your super hero name here eg the coder ': 90}
# find max Power points
# Most_powerful_hero = max(Power_points,key = Power_points.get)
# split first and last
# first name
# last name
# full = last name + " " +first name
# hero_name = full name.upper
# coder the real name
# email
# email password
# code is below use as it is 

import smtplib
name1 = ['Spider-Man', 'Captain America', 'Thor', 'Iron Man']
name2 = ['The Hulk', 'Black Panther', 'Doctor Strange']

print ("Superhero names in list 1 are:",name1)
print ("Superhero names in list 2 are:",name2)

name3 = name1 + name2
print ("Superhero names in list 3 are:",name3)


name3.append('Amough Goyal')
name3.remove('Doctor Strange')
print ("Names of all superheros are:",name3)

Power_points = {'Spider-Man': 70, 'Captain America': 70, 'The Thor': 85, 'Iron Man': 50, 'The Hulk': 70,
                'Black Panther': 66,
                'Amough Goyal': 90}
print ("Power of superheros acc to experts:",Power_points)


Most_powerful_hero = max(Power_points, key=Power_points.get)
print ("But most powerfull superhero is",Most_powerful_hero)

f = Most_powerful_hero.split(' ')
first_name = f[0]
print("First name of most powerfull superhero is",first_name)

last_name = f[1]
print("Last name of most powerfull superhero is",last_name)

full_name = last_name + " " + first_name
print("Full name of most powerfull superhero is",full_name)

hero_name = full_name.upper
print("Hero name of most powerfull superhero is",hero_name)


coder_name = first_name + " " + last_name
print("Coder name of ths prog is",coder_name)


gmail_user = "amoughgoyal3@gmail.com"
gmail_pwd = "passwordis2613"
TO = ['shantam1230@gmail.com']
SUBJECT = "Bonus task by Amough Goyal "
TEXT = "Testing...... sending mail using Gmail with the help of python..." + hero_name + " Link to your branch file here"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_user, gmail_pwd)
for i in range(len(TO)):
    BODY = '\r\n'.join(['To: %s' % TO[i],
                        'From: %s' % gmail_user,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

    server.sendmail(gmail_user, [TO[i]], BODY)
    print('email sent to '+ str(TO[i]))

server.close()

