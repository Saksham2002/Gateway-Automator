import yaml 

username = input("Enter your bennett enrollment without @bennett.edu.in--> ")
username+= "@bennett.edu.in"
password = input("Enter your bennett password for "+username+" --> ")


with open('logindetails.yml', 'w') as file:
    yaml.dump({"net_user":{"email": username, "password": password}}, file)
