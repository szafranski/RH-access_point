# RH-access_point
additional simple instruction how to make RotorHazard race timer on raspberry without using external router

The best moment to do that is after installation when you still have internet access on your raspberry.
  
In terminal (SSH):
________________

curl -sL https://install.raspap.com | bash -s -- -y
________________

(takes several minutes)
________________
sudo reboot
________________

connect to WiFi: raspi-webgui

password: ChangeMe<br/>



enter IP address: 10.3.141.1 in browser

Username: admin

Password: secret<br/>  


Click:
Configure hotspot -> SSID (enter name you want, eg. NEW_NAME) 

Wireless Mode (change to 802.11g - 2.4GHz)

save settings  

Click:
Configure hotspot -> security tab

PSK (enter password that you want to have, eg. NEW_PASS)

save settings

DON'T CHANGE OTHER SETTINGS IN GUI!  


in terminal (SSH):

________________

sudo nano /etc/dhcpcd.conf

add at the end of file (or change last lines accordingly):
________________

interface wlan0<br/>
static ip_address=2.2.2.2/24<br/>
static routers=2.2.2.2<br/>

static domain_name_server=1.1.1.1 8.8.8.8<br/><br/>

interface eth0<br/>
static ip_address=3.3.3.3/24<br/>
static routers=3.3.3.3<br/>

static domain_name_server=1.1.1.1 8.8.8.8
________________

and save (Ctrl+X -> y -> enter)

in terminal (SSH):

sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig<br/>

sudo nano /etc/dnsmasq.conf

and change the file so it looks like:
________________

interface=wlan0<br/>
dhcp-range=2.2.2.2,2.2.2.255,255.255.255.0,24h

interface=eth0<br/>
dhcp-range=3.3.3.4,3.3.3.255,255.255.255.0,24h
________________

and save (Ctrl+X -> y -> enter)

in terminal (SSH):
sudo reboot + disconnect raspberry from the router if it was connected

  
connect to WiFi: NEW_NAME
password: NEW_PASS
if you have any problems connecting wifi with new name - try "forgetting the (old) network in WiFi settings" and than try again

Now you should be able to enter the network using WiFi entering 2.2.2.2:5000 in the browser when WiFi is connected
or using ethernet entering 3.3.3.3:5000 in the browser. 


You can change network name and password entering 2.2.2.2 and logging using:
Username: admin
Password: secret
You can change this logging info Configure Auth in the gui if you want.


IMPORTANT! Don't connect ethernet cable to any DHCP-server capable device like another router or don't use WiFi client mode after this configuration.
It would mess it up.
