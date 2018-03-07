def bday():
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

def CleaningCalendar():
	#!/usr/bin/env python

	#Based on https://github.com/mattsage/CleaningCalendar
	
	import datetime
	
	datetoday = datetime.datetime.now().strftime('%A %d %B') #Todays Date e.g. Monday 13 June
	daynumber = datetime.datetime.now().day #Day Number of Month
	weeknumber = (daynumber - 1) // 7 + 1 #Week number of the Month 1-5
	weekday = datetime.date.today().strftime("%A") #Weekday e.g.Tuesday
	month = datetime.date.today().strftime("%B") #Month e.g. June
	
	#Daily Chore to do everyday
	dailychore = "De-Clutter living spaces, Wash up, Wipe kitchen surfaces"
	
	if weekday=="Monday":
		chore = "Hoover"
	if weekday=="Tuesday":
		chore = "Washing"
	if weekday=="Wednesday":
		chore = "Dust surfaces"
	if weekday=="Thursday":
		chore = "Bathrooms"
	if weekday=="Friday":
		chore = "Clear Fridge"
	if weekday=="Saturday":
		chore = "Catch-up"
  if weekday=="Sunday":
		chore = "WOMChore" #Week of the month chore
		
	if chore == "WOMChore": #Looks at week number for the Monthly Chore
		if weeknumber == 1:
			chore = "Appliances"
		elif weeknumber == 2:
			chore = "Furniture/Cabinets"
		elif weeknumber == 3:
			chore = "Windows & Doors"
		elif weeknumber == 4:
			chore = "MOYChore" #Month of the year Chore - Once per year
		else:
			chore = "Day Off!" #Last Sunday of the month off
	
	if chore == "MOYChore": #Looks at the Month
		if month=="January":
			chore = "Kitchen"
		elif month=="February":
			chore = "Cupboards"
		elif month=="March":
			chore = "Bathroom"
		elif month=="April":
			chore = "Garage"
		elif month=="May":
			chore = "Outside"
		elif month=="June":
			chore = "Mouldings and Doors"
		elif month=="July":
			chore = "Carpets"
		elif month=="August":
			chore = "Garden"
		elif month=="September":
			chore = "Windows"
		elif month=="October":
			chore = "Garage"
		elif month=="November":
			chore = "Fridge/Oven"
		elif month=="December":
			chore = "Mouldings and Doors"	
  return chore
