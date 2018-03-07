import inkyphat
from PIL import ImageFont, Image
import datetime
import subprocess

#Font Sizes
Datefont = ImageFont.truetype(inkyphat.fonts.FredokaOne, 19)
font2 = ImageFont.truetype(inkyphat.fonts.FredokaOne, 20)
font3 = ImageFont.truetype(inkyphat.fonts.FredokaOne, 17)

##################
#Date
##################
day = datetime.date.today().strftime("%A")
number = datetime.date.today().strftime("%-d")
mon = datetime.date.today().strftime("%b")
Tdate = day + " " +  number + " " + mon
w, h = font.getsize(Tdate)
Tdatex = (inkyphat.WIDTH / 2) - (w / 2)
Tdatey = (inkyphat.HEIGHT / 6) - (h / 2)

##################
#Chore
##################
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
	chore = "Dust"
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
		chore = "Windows and Doors"
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
		chore = "Windows & Sills"
	elif month=="October":
		chore = "Clear Garage"
	elif month=="November":
		chore = "Fridge/Oven"
	elif month=="December":
		chore = "Mouldings and Doors"	
w, h = font.getsize(chore)
chorex = (inkyphat.WIDTH / 2) - (w / 2)
chorey = (inkyphat.HEIGHT / 2) - (h / 2)

##################
#Weather
##################
#forecast = "Rain (H26C, L-1C)"
subprocess.call("/home/pi/SmartFrame/Get-Weather.sh", shell=True)

condition = subprocess.check_output("pywu forecast condition", shell=True) #Get Weather Condition
condition = condition.replace("\n", "")

low = subprocess.check_output("pywu forecast low_c", shell=True) #Get Temp Low
low = low.replace("\n", "")
low = low + "C"

high = subprocess.check_output("pywu forecast high_c", shell=True) #Get Temp High
high = high.replace("\n", "")
high = high + "C"
forecast = "%s (H %s, L %s" % (condition,high,low)

w, h = font.getsize(forecast)
forecastx = (inkyphat.WIDTH / 2) - (w / 2)
forecasty = (inkyphat.HEIGHT - 15) - (h / 2)

##################
#Display Text
##################
inkyphat.text((Tdatex, Tdatey), Tdate, inkyphat.BLACK, Datefont)
inkyphat.text((chorex, chorey), chore, inkyphat.RED, font2)
inkyphat.text((forecastx, forecasty), weather, inkyphat.BLACK, font3)
inkyphat.show()
