from datetime import *
from pushbullet import Pushbullet

###Pushbullet###
api_key = open('/home/pi/APIConfigs/Pushbulletkey.config', 'r').read() #read Pushbullet Key from /home/pi/Pushbulletkey.config file
api_key = api_key.replace("\n", "") #Remove Whitespace
#print api_key
pb = Pushbullet(api_key) 

####Dates####
currentDay= datetime.now().day
currentMonth= datetime.now().month
cdaymon= str(currentDay) + str(currentMonth)
#print currentDay
#print currentMonth
#print cdaymon

###LEDs###
#LED1 (Purple) - Person1

#LED2 (Blue) - Person2

#LED3 (Green) - Person3

#LED4 (Orange) - Person4

#LED5 (Pink) - Person5

#LED6 (RGB) - Other Birthday

#LED7 (White) - Other Event

#Birthdays daymon
person1 = "202" #20th Feb(2)
person2 = "12"
person3 = "13"
person4 = "14"
person5 = "15"
otherBday = ["62", "173", "202"]
xmas = "2512"
other = ["142", "107", "2610", "1712"] #Valentines etc

if cdaymon == person1:
	print "Happy Bday Person1"
	#LED1 On
	pbsubject = "Person1's Birthday Today"
	push = pb.push_note(pbsubject, pbsubject)
if cdaymon == person2:
	print "Happy Bday Person2"
	#LED2 on
	pbsubject = "Person2's Birthday Today"
	push = pb.push_note(pbsubject, pbsubject)
if cdaymon == person3:
	print "Happy Bday Person3"
	#LED3 On
	pbsubject = "Person3's Birthday Today"
	push = pb.push_note(pbsubject, pbsubject)
if cdaymon == person4:
	print "Happy Bday Person4"
	#LED4 On
	pbsubject = "Person4's Birthday Today"
	push = pb.push_note(pbsubject, pbsubject)
if cdaymon == person5:
	print "Happy Bday Person25"
	#LED5 On
	pbsubject = "Person5's Birthday Today"
	push = pb.push_note(pbsubject, pbsubject)
if cdaymon in otherBday:
	print "Other Bday"
	#LED6 On
	pbsubject = "Its a Loved Ones Birthday Today"
	push = pb.push_note(pbsubject, pbsubject)
if cdaymon in other:
	print "other event"
	#LED7 On
	pbsubject = "Its an Other event today! Check your Calendar!"
	push = pb.push_note(pbsubject, pbsubject)
if cdaymon == xmas:
	print "Merry Christmas"
	#All LEDs on and Flash
