# SmartFrame  
Heard of a digital photo frame?.....This one is SMART!  

SmartFrame is a Successer of my tried and tested [RouterPi](https://github.com/mattsage/RouterPi) but housed within a Photo Frame  

## SmartFrame offers:
#### Blinkt!  
* Travel Times  
* Internet Speed Tests 
* VPN  
* Transmission Active  
* Litecoin  
* Ripple
#### Inky pHat  
* Date  
* Chore Calendar  
* Weather  
#### LEDs  
* LED Notification of Important Dates and Birthdays  
#### Other
* Pi-Hole  
* Xmas Countdown  

## Timings  
* 0000 - 
* 

## Hardware:
* Raspberry Pi Zero W  
* Pico Hat Hack4r (https://shop.pimoroni.com/products/pico-hat-hacker)  
* Inky Phat (https://shop.pimoroni.com/products/inky-phat)  
* Blinkt! (https://shop.pimoroni.com/products/blinkt)  
* Numerous LEDs of different Colours (https://thepihut.com/products/ultimate-3mm-led-kit)  
* Push Buttons  
* Jumper Cables  
* Photo Frame  

## Setup:  
Create /home/pi/APIConfigs  

## Scripts Description:  
* BdayChecker.py - Checks for a Birthday or other event and sends PushBullet Notification and lights corresponding LED in picture  

## GPIOs Used:  
#??, #?? - Inky Phat  
#??, #?? - Blinkt!  
#?? - Button on/off  
#?? - Button VPN  
#?? - LED1 (Purple)  
#?? - LED2 (Blue)  
#?? - LED3 (Green)  
#?? - LED4 (Orange)   
#?? - LED5 (Pink)  
#?? - LED6 (RGB)    
#?? - LED7 (White)  

### Blinkt! LEDs
1) My Traffic  
2) Wife's Traffic  
3) Internet Down?  
4) VPN On  
5) Download Complete  
6)  
7)  
8)  

## API Keys needed:  
#Github Key  
/home/pi/APIConfigs/github.config  

#Home Coords for Traffic  
/home/pi/APIConfigs/Home.config  

#IFTTT Key for GSheets  
/home/pi/APIConfigs/IFTTT-Makerkey.config  

#Pushbullet Key  
/home/pi/APIConfigs/Pushbulletkey.config  

#Gooogle Maps API Key for Traffic  
/home/pi/APIConfigs/MapsAPI.config  

#Work Coords for Traffic  
/home/pi/APIConfigs/Work.config  

#Weather Underground API Key  
/home/pi/APIConfigs/WUapikey.config  

#Home Location for Weather  
/home/pi/APIConfigs/Wulocation.config  
