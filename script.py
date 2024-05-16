# import required libraries and modules
import sys
from jinja2 import Environment, FileSystemLoader
import yaml
from netmiko import ConnectHandler
from datetime import datetime



# Greeting
greeting = f"""*******************************************************************************
         ****************************************************
                      **********************
********** Welcome to THE BEST NETWORK AUTOMATION program ***********
           ********** This Lozy here to help you **********
                Today is {datetime.day}/{datetime.month}/{datetime.year}
                     let's start our journey ^___^ 
*******************************************************************************
         ****************************************************
                      **********************                  

"""

print(greeting)

# configration options (OSPF, BGP, STATIC)
options = sys.argv
print(f"You choose NUMBER {options[1]} of the configration mode \n 1 for OSPF,  2 for BGP,  3 for Static \n \n \n")


# open jinja
env = Environment(loader=FileSystemLoader("."))


if options[1] == "1":
    temp = env.get_template("ospf.j2")
    with open("input_ospf.yml") as file:
        ospf_yaml = yaml.load(file, Loader=yaml.FullLoader)

    config = temp.render(int=ospf_yaml)


elif options[1] == "2":
    temp = env.get_template("BGP.j2")
    with open("input_BGP.yml") as file:
        bgp_yaml = yaml.load(file, Loader=yaml.FullLoader)

    config = temp.render(int=bgp_yaml)

elif options[1] == "3":
    temp = env.get_template("static.j2")
    with open("input_static.yml") as file:
        static_yaml = yaml.load(file, Loader=yaml.FullLoader)

    config = temp.render(int=static_yaml)

else:
    print("Error! \n Please try again.")

# SSH using Netmiko
if config:
    vxr = ConnectHandler(host="192.168.240.47", username="router1", password="router1@nti", device_type="cisco_ios")
    vxr.enable()
    vxr.send_command_timing("conf t")
    show = vxr.send_command_timing(config)
    print("This is the output: \n \n" +show)
