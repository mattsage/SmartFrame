from datetime import *
from pushbullet import Pushbullet
from gpiozero import LED

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
LED1 = LED(25) #Pin25
#LED2 (Blue) - Person2
LED2 = LED(??) #Pin??
#LED3 (Green) - Person3
LED3 = LED(??) #Pin??
#LED4 (Orange) - Person4
LED4 = LED(??) #Pin??
#LED5 (Pink) - Person5
LED5 = LED(??) #Pin??
#LED6 (RGB) - Other Birthday
LED6 = LED(??) #Pin??
#LED7 (White) - Other Event
LED7 = LED(??) #Pin??

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
	#LED1.on()
	pbsubject = "Person1's Birthday Today"
	push = pb.push_note(pbsubject, pbsubject)
if cdaymon == person2:
	print "Happy Bday Person2"
	#LED2.on()
	pbsubject = "Person2's Birthday Today"
	push = pb.push_note(pbsubject, pbsubject)
if cdaymon == person3:
	print "Happy Bday Person3"
	#LED3.on()
	pbsubject = "Person3's Birthday Today"
	push = pb.push_note(pbsubject, pbsubject)
if cdaymon == person4:
	print "Happy Bday Person4"
	#LED4.on()
	pbsubject = "Person4's Birthday Today"
	push = pb.push_note(pbsubject, pbsubject)
if cdaymon == person5:
	print "Happy Bday Person25"
	#LED5.on()
	pbsubject = "Person5's Birthday Today"
	push = pb.push_note(pbsubject, pbsubject)
if cdaymon in otherBday:
	print "Other Bday"
	#LED6.on()
	pbsubject = "Its a Loved Ones Birthday Today"
	push = pb.push_note(pbsubject, pbsubject)
if cdaymon in other:
	print "other event"
	#LED7.on()
	pbsubject = "Its an Other event today! Check your Calendar!"
	push = pb.push_note(pbsubject, pbsubject)
if cdaymon == xmas:
	print "Merry Christmas"
	#LED1.on()
	#LED2.on()
	#LED3.on()
	#LED4.on()
	#LED5.on()
	#LED6.on()
	#LED7.on()
