This is for Linux PCs, the program has only been tested on a Kali host.
Your results may be diffrent. You have been warned. Use at your own risk.

Place this dir the 'MACInstall' in your home dir '~/' or /home/YourUserName/

Run the makeinstall file like so './makeinstall' this should make them 
exacutable from the terminal. Make sure you have run this first! If you don't
remember your MAC address or it wasn't saved don't worry, just restart your PC.

To get a new mac use 'macauto', to go back to your old mac use 'macback',
to show what your mac is use 'macshow'.

I would recommend running the 'MACWait' while not connected to a network,
this is due to the DHCP and how it will deal with a 'new' request from 
what it views as a new host conected to the network. 

The 'macauto' will automatically assign you a MAC address and the DHCP will
assign you a new IP address on that network. 

The 'macauto' can be used in conjunction with the tor network. This will mask
your MAC/IP to the first router. From there the router's MAC/WAN IP addresses
will be used. 
