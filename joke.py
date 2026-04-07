if __name__ != "__main__":
    import requests
    import os
    import json

    print("Fetching a joke...")
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    #print the joke
    if response.status_code == 200:
        joke = response.json()
        print(f"{joke['setup']} - {joke['punchline']}")
    else:
        print("Failed to fetch a joke. Please try again later.")
else:
    print("Please run this command from the main magOS file. and not directly.")
