# External imports
from pyzabbix import ZabbixAPI
from termcolor import colored
import os, sys

def menu():
    os.system('clear')
    print(colored(
        "---------------------- WELCOME TO DATA EXTRACTION ----------------------\n"
        "-- This script is based on the use of API contained in the official Zabbix documentation --\n"
        "-- The goal is to extract the number of alarms and how many have been resolved with or without technical intervention --\n"
        "-- Developed by Nathan Quadros Silva - 03/02/2021 --\n"
        "-- Doubts or concerns contato@nathanqsilva.com.br or https://nathanqsilva.com.br --\n", 'blue'
    ))
    print()
    print()
    print(colored(
        "-- Select an optioin --",'yellow', attrs=['bold']
    ))
    print("[1] - Exec")
    print("[0] - Exit")
    menu_option()
    
def menu_option():
    option = input("+ Select an option: ")
    if option == '1':
        exec()
    elif option == '0':
        sys.exit()
    else:
        menu()

def exec():
    print()
    print(colored(
        "** Enter login **",'red',attrs=['bold']
    ))
    server = input("+ Enter your server: ")
    user = input("+ Enter your username: ")
    password = input("+ Type your password: ")

    os.system('clear')
    
    zapi = ZabbixAPI(server)
    zapi.login(user, password)

    print(colored("**Login successful**",'blue'))
    print()
    print(colored("-- Enter the timestamp values ​​(visit https://www.epochconverter.com/ to convert to timestamp) --", 'red', attrs=['bold']))
    print(colored("-- In brazil use add +3 in the hours --", 'red', attrs=['bold']))
    print()
    print()
    timeFrom = input("+ Select time from: ")
    timetill = input("+ Select time till: ")

    events = zapi.event.get(
        output= ['eventid','acknowledged','r_eventid'],
        time_from= timeFrom,
        time_till= timetill
    )

    contEvent = 0
    contResolv = 0
    contAck = 0

    for event in events:
        resolved = event['r_eventid']
        ack = event['acknowledged']
        
        contEvent += 1
        
        if resolved != '0':
            contResolv += 1
        
        if ack == '1':
            contAck += 1

    os.system('clear')
    print(colored("-- Success --",'green',attrs=['bold']))
    print(colored("****",'blue', attrs=['bold'])," De "+colored(str(contEvent), 'yellow', attrs=['bold'])+" alarmes, foram resolvidos "+colored(str(contResolv), 'yellow', attrs=['bold'])+" sendo, "+colored(str(contAck), 'yellow', attrs=['bold'])+" com alguma intervenção tecnica ",colored("****",'blue', attrs=['bold']))
    print()
    print()
    input("Press ENTER to continue")
    zapi.user.logout()
    menu()
    
if __name__ == '__main__':
    menu()