# CoD-VPN-Patcher
Patches OpenVPN/WireGuard Profiles (.ovpn/.conf) to CoD VPN profiles.

# Warining
This is something I've put together in a few minutes! It probably works with most/all OpenVPN/WireGuard profiles but that is not guaranteed. Use it at your own risk!

## Requirements
1. A VPN provider that offers .ovpn or .conf files to download (e.g. NordVPN)
2. The newest version of [OpenVPN](https://openvpn.net/community-downloads/) or [WireGuard](https://www.wireguard.com/install/)
3. [Python](https://www.python.org/downloads/) 3.9 or higher, check your Python version by opening a Terminal and typing "python --version" (only tested on python 3.11.6, should work tho)

## Installation
1. Download this repository as .zip
2. Extract the folder and drag it somewhere it belongs (e.g. your programs folder)
3. (optional) For easier access you can create a shortcut for the .bat file and put it on your Desktop
4. Download .ovpn/.conf file of your VPN provider
5. Drag the VPN file over the "CoD VPN Patcher.bat" file or the shortcut
6. A new file will be created with the name "\<original file name>_CoD_VPN.\<ovpn/conf>"
7. Import the new VPN file into OpenVPN/WireGuard
8. Profit?
