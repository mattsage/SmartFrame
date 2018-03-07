import inkyphat
from Functions_SmartFrame import *
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
chore = CleaningCalendar()
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
