#Neofetch

Neofetch is a CLI system information tool which displays information about your operating system, software and hardware in an aesthetic and visually pleasing way.
The overall purpose of Neofetch is to be used in screen-shots of your system. Neofetch shows the information other people want to see. 
You can further configure Neofetch to display exactly what you want it to. Through the use of command-line flags and the configuration file you can change existing information outputs or add your own custom ones
It supports various operating systems from Linux to Windows, all the way to more obscure operating systems like Minix, AIX and Haiku.

##Features
-Display info about OS,software,hardware
-Configure information
-Supports various operating softwares

##Setup Instructions
1. Clone the Repository:
```bash
git clone https://github.com/dylanaraps/neofetch.git
cd neofetch
```
2. Crete a Virtual Environment:
```bash
python3 -m venv name-of-env
source name-of-env/bin/activate
```
3. Install Neofetch using ```bash make install```:
-MacOS - ```bash make PREFIX=/usr/local install```
-Haiku - ```bash make PREFIX=/boot/home/config/non-packaged install```
-OpenIndiana - ```bash gmake install``
-Windows - ```bash scoop install neofetch```
NOTE - This is optional

###Usage
-Get Info - Gets information about your OS, software or hardware
-Configure Information - Configure what info should be displayed
###Reeport Issues
If your OS isn't supported then open an issue and it will be added