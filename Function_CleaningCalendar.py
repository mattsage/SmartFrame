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
