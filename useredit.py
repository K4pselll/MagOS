print("account information:")
import os
import json
with open("SYS/loginmgr.json") as f:
    jsonp = json.load(f)
username = os.getlogin()
password = jsonp["details"]["password"]
print("Edit your current account information:")
print("leave blank for no change.")
new_username = input(f"Username ({username}): ")
if new_username != "":
    username = new_username
else:
    print("Skipped.")
new_password = input("Password: ")
if new_password != "":
    password = new_password
else:
    print("Skipped.")
print("Saving changes...")
jsonp["details"]["username"] = username
jsonp["details"]["password"] = password
with open("SYS/loginmgr.json", "w") as f:
    json.dump(jsonp, f)
print("Changes saved.")
