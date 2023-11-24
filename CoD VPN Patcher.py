import sys
from tkinter import messagebox

NAME = "CoD VPN Patcher"
def error(msg):
    messagebox.showerror(NAME, msg)
    exit(1)

if (len(sys.argv) == 1 or len(sys.argv) >= 3):
    error("Drag an (.ovpn) file over the (.bat) file to patch it")

if (sys.argv[1].split('.')[-1] != "ovpn"):
    error("Not the correct file type. (.ovpn file needed)")

vpn_file = sys.argv[1]
f = open(vpn_file, "r")
splitted_file = f.read().split("<ca>")

if ("route-nopull\nroute 185.34.0.0 255.255.0.0" in splitted_file[0]):
    error("(.opvn) File is already patched")

splitted_file[0] += "route-nopull\nroute 185.34.0.0 255.255.0.0\n<ca>" # Adding modification to VPN file
patched_vpn_file = ""
for splitter in splitted_file: # Reassemnling content of VPN File
    patched_vpn_file += splitter

f.close()
f = open(vpn_file.split(".ovpn")[0] + "_CoD_VPN.ovpn", "w")
f.write(patched_vpn_file)
f.close()
messagebox.showinfo(NAME, "Successfully patched!")
exit(0)
