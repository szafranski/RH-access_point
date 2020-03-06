from time import sleep
import os
import sys
import json

if os.path.exists("./updater-config.json") == True:
	with open('updater-config.json') as config_file:
		data = json.load(config_file)
else:
	with open('distr-updater-config.json') as config_file:
		data = json.load(config_file)

if data['debug_mode'] == 1:
	linux_testing = True
else:
	linux_testing = False 
if linux_testing == True:
	user = data['debug_user']
else:
	user = data['pi_user']

myPlace = data['country']

class bcolors:
	HEADER = '\033[95m'
	ORANGE = '\033[33m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def image():
	print("""
\t                               **/(((/**                              
\t                            */###########(*                           
\t                          */#####@@@@@#####(*                         
\t                         *(((((@@@###@@@#####*,                       
\t                       */((((@@@#######@@@####/*                      
\t                      *(((((@@@(((((#(##@@@#####*                     
\t                    **((((&@@&((((*...####@@@####**                   
\t                   *(((((@@@((((((....((((#@@@#####*                  
\t                 **((((#@@@((((((*.....((((#%@@&####/*                
\t                */((((@@@((((((((......(((((((@@@####(*               
\t              .*(((((@@@(((((((((......((((((((@@@%####**             
\t             */((((@@@(((((((((((......((((((((((@@@####(*            
\t            *(((((@@@((((((((((((.....*(((((((((((@@@#####*,          
\t          **((((@@@((((((((((((((.....((((((((((((((@@@(#(#/*         
\t          *((((@@@(((((((((((((((.....(((((((((((((((@@@((###*        
\t       */((((&@@&(((((((((((((,...(((....(((((((((((((#@@@((((/*      
\t      */((((@@@(((((((((......................((((((((((@@@((((#*     
\t    .*//(((@@@((((((............(((((((*.........,(((((((%@@&((((/*   
\t   */////@@@(((((........../((((((((((((((*..........((((((@@@(((((*  
\t  */////@@@/(((......./(((((((((((((((((((((((/......../((((@@@#((((*.
\t *////%@@/////(((((((((((((((((((((((((((((((((((((((..(((((((@@@((((*
\t *////@@@/////////((((((((((((((((((((((((((((((((((((((((((((@@@((((*
\t **/////@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#((((**
\t  ***/////////////////(((((((((((((((((((((((((((((((((((((((((((((** 
\t     ****////////////////((((((((((((((((((((((((((((((((((((/****    
""")

def logoTop():
	print("""\n	
		#######################################################################
		###                                                                 ###
		###\t\t\t"""+bcolors.ORANGE+"""     RotorHazard        """+bcolors.ENDC+"""\t\t    ###
		###                                                                 ###
		###                     OTA Updater and Manager                     ###
		###                                                                 ###
		#######################################################################""")
	if (linux_testing == True):
		print("\t\t\t\t\t  Linux PC version")
	if os.path.exists("./updater-config.json") == False:
		print("\t\t\t    Looks that you haven't set up config file yet!")

def first ():
	image ()
	os.system("clear")
	print("\n")
	image()
	sleep(0.5)
first()

# Set the WiFi country in raspi-config's Localisation Options:
# sudo raspi-config
# ( 4. point -> I4 - Change WiFi country -> select -> enter -> finish )

def stepFour():

	print("""Step 4.""")

	print("""
Connect PC to WiFi network:
name: RH-TIMER
password: timerpass
if you have any problems connecting wifi with new name - try "forgetting" the (old) network in PC's WiFi settings and than try again

Now you should be able to enter the network typing in the browser:
10.10.10.10:5000 - using WiFi
172.20.20.20:5000 - using ethernet.""")

	print("""\n\t\t\t\t"""+bcolors.GREEN+"""    Reboot by pressing 'r' """+bcolors.ENDC+"""\n\n\t\t\t\t"""
			+bcolors.YELLOW+"""    Exit by pressing 'e'"""+bcolors.ENDC+"""\n""")
	selection=str(raw_input(""))
	if selection=='r':
		os.system("sudo reboot")
	if selection=='e':
		sys.exit()
	else :
		main()

def stepThree():

	print("""\n\t\tStep 3.\n""")
	os.system("sudo mv /etc/dhcpcd.conf /etc/dhcpcd.conf.orig")
	os.system("sudo cp ./net_ap/dhcpcd.conf.ap /etc/dhcpcd.conf")
	os.system("sudo cp /etc/dhcpcd.conf /etc/dhcpcd.conf.ap")
	os.system("sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig")
	os.system("sudo cp ./net_ap/dnsmasq.conf.ap /etc/dnsmasq.conf")
	os.system("sudo cp /etc/dnsmasq.conf /etc/dnsmasq.conf.ap")
	print("""\n\tAfter rebooting you can connect to the timer, via Wifi or ethernet.\n 
	WiFi: 10.10.10.10:5000 (10.10.10.10:5000 if connecting from a browser)
	ethernet: 172.20.20.20 (172.20.20.20:5000 if connecting from a browser)\n\n
	You can enter access point extra menu after rebooing
	and check how you can connect to the internet.\n""")
	print("""\n\t\t\t\t"""+bcolors.GREEN+"""    Reboot by pressing 'r' """+bcolors.ENDC+"""\n\n\t\t\t\t"""
			+bcolors.YELLOW+"""    Exit by pressing 'e'"""+bcolors.ENDC+"""\n""")
	selection=str(raw_input(""))
	if selection=='r':
		os.system("sudo reboot")
	if selection=='e':
		sys.exit()
	else :
		main()

def stepTwo():
	print("""\n\n
	Step 2.\n
Next step would require performing some actions in GUI.
You may write those informations down or take a picture etc.
You can also print file 'step_two.txt' from 'net_ap' folder.
Remember to do it BEFORE rebooting.
After performing step 2. and connecting to timer again, 
come back to this menu and enter step 3.
	
connect PC to WiFi network: 
name: raspi-webgui
password: ChangeMe

enter IP address: 10.3.141.1 in browser
Username: admin
Password: secret  

Click:
Configure hotspot -> SSID (enter name you want, eg. "RH-TIMER") 

Wireless Mode (change to 802.11n - 2.4GHz)

save settings 

Click:
Configure hotspot -> security tab

PSK (enter password that you want to have, eg. "timerpass")

save settings

DON'T CHANGE OTHER SETTINGS IN GUI!  


Read carefully whole instruction from above before rebooting!""")

def stepOne():
#	os.system("sudo sed -i 's/country/# country/g' /etc/wpa_supplicant/wpa_supplicant.conf")
#	os.system("echo 'country="+myPlace+"'| sudo  tee -a /boot/config.txt")
#	os.system("sudo apt-get update && sudo apt-get upgrade -y")
	os.system("sudo apt install curl -y")
#	os.system("curl -sL https://install.raspap.com | bash -s -- -y")
	stepTwo()
	print("""\n\t\t\t\t"""+bcolors.GREEN+"""Reboot by pressing 'r' """+bcolors.ENDC+"""\n\n\t\t\t\t"""
			+bcolors.YELLOW+"""Exit by pressing 'e'"""+bcolors.ENDC+"""\n""")
	selection=str(raw_input(""))
	if selection=='r':
		os.system("sudo reboot")
	if selection=='e':
		sys.exit()
	else :
		main()

def stepZero():
	sleep(0.12)
	os.system("clear")
	sleep(0.12)
	logoTop()
	sleep(0.12)
	print("""\n\n
	After performing this process your Raspberry Pi can be used as standalone\n
	Access Point. You won't need additional router for connecting with it. \n
	You will loose ability of connecting Raspberry wirelessly to any router or hotspot.\n
	You will still have ability to connect it to the Internet sharing device, \n
	like router or PC via ethernet cable. You will also be able to connect with the timer\n
	via Wifi from PC or mobile phone etc. - if you had range. \n\n
	This process will require few reboots. Do you want to continue?\n""")
	print("""\n
	\t\t"""+bcolors.GREEN+"""'y' - Yes, let's do it """+bcolors.ENDC+"""\n
	\t\t'3' - enters "Step 3." - check it later\n
	\t\t'x' - enters access point extra menu - check it later\n
	\t\t"""+bcolors.YELLOW+"""'e' - exit to main menu"""+bcolors.ENDC+"""\n""")
	selection=str(raw_input(""))
	if selection=='y':
		stepOne()
	if selection=='3':
		stepThree()
	if selection=='x':
		apMenu()
	if selection=='e':
		sys.exit()
	else :
		main()


def stepFive():

	print("""Step 5.""")
	os.system("echo 'interface wlan0' | sudo tee -a /etc/dhcpcd.conf.net")
	os.system("echo 'static ip_address=10.10.10.10/24' | sudo tee -a /etc/dhcpcd.conf.conf.net")
	os.system("echo 'static routers=10.10.10.10' | sudo tee -a /etc/dhcpcd.conf.conf.net")
	os.system("echo 'static domain_name_server=1.1.1.1 8.8.8.8' | sudo tee -a /etc/dhcpcd.conf.conf.net")
	os.system("echo ' ' | sudo tee -a /etc/dhcpcd.conf.net")
	os.system("echo 'interface eth0' | sudo tee -a /etc/dhcpcd.conf.net")
	os.system("echo '#static ip_address=172.20.20.20/20' | sudo tee -a /etc/dhcpcd.conf.net")
	os.system("echo '#static routers=172.20.20.20' | sudo tee -a /etc/dhcpcd.conf.net")
	os.system("echo '#static domain_name_server=1.1.1.1 8.8.8.8' | sudo tee -a /etc/dhcpcd.conf.net")

def end():
		os.system("clear")
		print("\n\n")
		image()
		sleep(0.5)
		os.system("clear")
		sys.exit()

def apConf():
	os.system("sudo cp /etc/dhcpcd.netap /etc/dhcpcd.conf")
	print("""\n\t\t\t\t"""+bcolors.GREEN+"""    Reboot by pressing 'r' """+bcolors.ENDC+"""\n\t\t\t\t"""
			+bcolors.YELLOW+"""    Exit by pressing 'e'"""+bcolors.ENDC+"""\n""")
	selection=str(raw_input(""))
	if selection=='r':
		os.system("sudo reboot")
	if selection=='e':
		sys.exit()
	else :
		apConf()

def netConf():
	os.system("sudo cp /etc/dhcpcd.netap /etc/dhcpcd.conf")
	print("""\n\t\t\t\t"""+bcolors.GREEN+"""    Reboot by pressing 'r' """+bcolors.ENDC+"""\n\t\t\t\t"""
			+bcolors.YELLOW+"""    Exit by pressing 'e'"""+bcolors.ENDC+"""\n""")
	selection=str(raw_input(""))
	if selection=='r':
		os.system("sudo reboot")
	if selection=='e':
		sys.exit()
	else :
		netConf()

def main():
	stepZero()
	stepOne()
	stepTwo()
	stepThree()
	stepFour()
	stepFive()
	end()
main()