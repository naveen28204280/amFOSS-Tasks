#Documentation for Neofetch

##Overview
Neofetch is a command-line system information tool written in bash. Neofetch displays information about your operating system, software and hardware in an aesthetic and visually pleasing way.You can further configure Neofetch to display exactly what you want it to. Through the use of command-line flags and the configuration file you can change existing information outputs or add your own custom ones

##Functionality

###Displayed Information
-OS: Displays the operating system name and version
-Kernel: Shows the kernel version
-Uptime: Displays system uptime
-Packages: Counts and shows the number of installed packages
-Shell: Displays the default shell and its version
-Resolution: Shows the current screen resolution
-DE/WM: Displays the desktop environment or window manager in use
-Theme: Shows the active GTK and icon themes
-CPU: Displays the processor model and speed
-GPU: Shows graphics card information
-Memory: Displays used and available memory

###Key Commands

bash`neofetch`
Runs basic neofetch and displays system information
bash`neofetch --config /path/to/config.conf`
Runs neofetch but displays only the specified information
bash`neofetch --off`
Runs neofetch but doesn't dispay any information
bash`neofetch --ascii_distro "distro_name"`
Runs neofetch and overrides the ASCII logo with other’s logo

###Configuration

Users can configure what system information is displayed and customise it. Custom ASCII logos, colours can be configured in the configuration file

**Example**
-Show only CPU information
bash`neofetch --config none --cpu --memory`
-Show only ASCII logo
bash`neofetch --ascii /path/to/logo.txt`

###Installation Details

####Using Git(Only for MacOS, Linux)
-Open Terminal
-Enter this command
bash`git clone https://github.com/dylanaraps/neofetch.git`

####Using ZIP file
-Enter this link and open Github https://github.com/dylanaraps/neofetch
-Click on the green-coloured Code option
-Click on the Download ZIP option
-Now decompress the ZIP file