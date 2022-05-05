# Python program to create a website timer based login
# Import the webbrowser and time module 
import time
from selenium import webdriver
import yaml 
print("\n\n<======= INTERNET GATEWAY AUTOMATOR V1.0 =====>")
print("by Saksham.J\n")
try:
    conf = yaml.full_load(open('logindetails.yml')) 
except:
    username = input("Enter your bennett enrollment without @bennett.edu.in--> ")
    username+= "@bennett.edu.in"
    password = input("Enter your bennett password for "+username+" --> ")
    with open('logindetails.yml', 'w') as file:
        yaml.dump({"net_user":{"email": username, "password": password}}, file)

conf = yaml.full_load(open('logindetails.yml'))
buemail = conf['net_user']['email']
bupassword = conf['net_user']['password']

#Login-module
def login(url,usernameId, username, passwordId, password, submit_buttonId):
   driver = webdriver.Chrome()
   driver.get(url)
   driver.find_element_by_name(usernameId).send_keys(username)
   driver.find_element_by_name(passwordId).send_keys(password)
   driver.find_element_by_name(submit_buttonId).click()

# Taking website to be opened as input
# link  = input("Enter website to try->")
# link = "http://"+link
link = "http://172.16.16.16/24online/webpages/client.jsp"
opt = input("Right now or Timer based script? R (ight now) / T (imer)/ E (xit) ->")
if(opt=="R" or opt=="r"):
    login(link, "username", buemail, "password", bupassword, "login")
    exit()
if(opt=="E" or opt=="e"):
    print("Exiting........................bye bye!")
    time.sleep(2)
    exit()
# Taking alarm time from the user
alarm = input("At what time the login windows appears? (Format:- HH:MM:SS)(24 hour format) like 15:23:00 ->") 
  
# This is the actual time that we will use to print. 
Current_time = time.strftime("%H:%M:%S") 

# Printing current time until alarm time
while (True): 
    print ("Waiting, the current time is " + Current_time +" :-( " )
    Current_time = time.strftime("%H:%M:%S") 
    time.sleep(1) 
    # Opening the webpage at alarm time
    if (Current_time == alarm): 
        login(link, "username", buemail, "password", bupassword, "login")
    else:
        continue
