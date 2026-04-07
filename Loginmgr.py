
import os
import sys
import json

with open("SYS/loginmgr.json") as f:
    jsonp = json.load(f)
username = os.getlogin()
password = jsonp["details"]["password"]

class loginmgr:
    def login(self):
        print(username)
        if password != "":
            for i in range(3):
                tries = 3
                inputp = input("Password >> ")
                if inputp == password:
                    print("Welcome!")
                    return
                else:    
                    print("Wrong password.")
                    tries -= 1
                if tries == 0:
                    print("Too many attempts, exiting.")
                    sys.exit(0)
        else:
            print("Welcome!")
    
        
