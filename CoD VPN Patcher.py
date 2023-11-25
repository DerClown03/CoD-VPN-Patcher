import sys
from tkinter import messagebox

NAME = "CoD VPN Patcher"

def error(msg, file=""):
    messagebox.showerror(NAME, msg + "\n" + file)
    exit(1)

def patch_ovpn(path: str):
    f = open(path, "r")
    splitted_file = f.read().split("<ca>")

    if (len(splitted_file) <= 1):
        error("This (.ovpn) file can not be patched by " + NAME, path)

    if ("route-nopull\nroute 185.34.0.0 255.255.0.0" in splitted_file[0]):
        error("(.ovpn) File is already patched", path)

    splitted_file[0] += "route-nopull\nroute 185.34.0.0 255.255.0.0\n<ca>" # Adding modification to VPN file
    patched_vpn_file = ""
    for splitter in splitted_file: # Reassemnling content of VPN File
        patched_vpn_file += splitter

    f.close()
    new_vpn_file = path.split(".ovpn")[0] + "_CoD_VPN.ovpn"
    f = open(new_vpn_file, "w")
    f.write(patched_vpn_file)
    f.close()
    messagebox.showinfo(NAME, "Successfully patched!\nNew VPN profile at:\n" + new_vpn_file)
    exit(0)

def patch_wireguard(path: str):
    f = open(path, "r")
    vpn_text = f.read()
    if ("AllowedIPs = 185.34.0.0/16" in vpn_text):
        error("(.conf) File is already patched", path)

    if ("AllowedIPs = 0.0.0.0/0" in vpn_text):
        vpn_text = vpn_text.replace("0.0.0.0/0", "185.34.0.0/16")
        f.close()
        new_vpn_file = path.split(".conf")[0] + "_CoD_VPN.conf"
        f = open(new_vpn_file, "w")
        f.write(vpn_text)
        f.close()
        messagebox.showinfo(NAME, "Successfully patched!\nNew VPN profile at:\n" + new_vpn_file)
        exit(0)
    else:
        error(f"This (.conf) file can not be patched by " + NAME, path)


if (len(sys.argv) == 1 or len(sys.argv) >= 3):
    error("Drag an (.ovpn/.conf) file over the (.bat) file to patch it")

if (sys.argv[1].split('.')[-1] == "ovpn"):
    patch_ovpn(sys.argv[1])

if (sys.argv[1].split('.')[-1] == "conf"):
    patch_wireguard(sys.argv[1])

error("Not the correct file type. (.ovpn/.conf) file needed", sys.argv[1])
