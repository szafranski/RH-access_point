# RH-access_point
additional simple instruction how to make RotorHazard race timer on raspberry without using external router

The best moment to do that is after installation when you still have internet access on your raspberry.<br/><br/>

<br/> <br/>

Update raspberry - in terminal:

<br/>

sudo apt-get update
sudo apt-get dist-upgrade
sudo reboot

<br/>

Set the WiFi country in raspi-config's Localisation Options: sudo raspi-config

<br/>

  
In terminal (SSH):
________________

curl -sL https://install.raspap.com | bash -s -- -y
________________

(takes several minutes)
________________
sudo reboot
<br/>

________________
<br/>

connect to WiFi: raspi-webgui

password: ChangeMe<br/><br/><br/>





enter IP address: 10.3.141.1 in browser

Username: admin

Password: secret<br/>  <br/>



Click:
Configure hotspot -> SSID (enter name you want, eg. NEW_NAME) 

Wireless Mode (change to 802.11g - 2.4GHz)

save settings  
<br/>
<br/>

Click:
Configure hotspot -> security tab

PSK (enter password that you want to have, eg. NEW_PASS)

save settings
<br/>

DON'T CHANGE OTHER SETTINGS IN GUI!  
<br/>
<br/>


in terminal (SSH):

________________

sudo nano /etc/dhcpcd.conf

add at the end of file (or change last lines accordingly):
________________

interface wlan0<br/>
static ip_address=10.10.10.10/24</br>
static routers=10.10.10.10</br>

static domain_name_server=1.1.1.1 8.8.8.8<br/><br/>

interface eth0
static ip_address=172.20.20.20/20<br/>
static routers=172.20.20.20<br/>

static domain_name_server=1.1.1.1 8.8.8.8
________________

and save (Ctrl+X -> y -> enter)<br/>
<br/>


in terminal (SSH):

sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig<br/>

sudo nano /etc/dnsmasq.conf

and change the file so it looks like:
________________

interface=wlan0<br/>
  dhcp-range=10.10.10.11,10.10.10.255,255.255.255.0,24h
<br/>

interface=eth0<br/>
  dhcp-range=172.20.20.21,172.20.20.255,255.255.255.0,24h
________________

and save (Ctrl+X -> y -> enter)<br/>
<br/>


in terminal (SSH):
sudo reboot + disconnect raspberry from the router if it was connected
<br/>
<br/>

  
connect to WiFi: NEW_NAME <br/>
password: NEW_PASS <br/> <br/>
if you have any problems connecting wifi with new name - try "forgetting the (old) network in WiFi settings" and than try again

<br/> <br/>

Now you should be able to enter the network using WiFi entering 10.10.10.10:5000 in the browser when WiFi is connected
or using ethernet entering 172.20.20.20:5000 in the browser. 

<br/> <br/>

You can change network name and password entering 10.10.10.10 and logging using: <br/>
Username: admin <br/>
Password: secret <br/>
You can change this logging info Configure Auth in the gui if you want.

<br/> <br/>

IMPORTANT! Don't connect ethernet cable to any DHCP-server capable device like another router or don't use WiFi client mode after this configuration.
It would mess it up.
