def main():
    """Entry point for running magOS"""
    print("Starting magOS...")
    try:
        import colorama
        import requests
    except ImportError:
        import sys
        #just in case
        print("Could not start magOS. Missing modules.")
        print("Repairing...")
        os.system('.venv\\Scripts\\pip.exe install colorama requests pygame')
        print("Installed missing modules, please start magOS again.")
        sys.exit(0)

    import time
    import os
    import sys
    import json
    import requests
    import colorama
    from colorama import Fore
    from SYS import Loginmgr

    print("Welcome to magOS!")

    Loginmgr.loginmgr().login()
    print("Type 'help' for a list of commands.")
    while True:
        cmmds = os.listdir("commands")
        cmmds = [cmd.replace(".py", "") for cmd in cmmds if cmd.endswith(".py")]
        inputp = input(">> ")
        if inputp in cmmds:
            os.system(f'.venv\\Scripts\\python.exe commands/{inputp}.py')
        elif inputp == "exit":
            print("Exiting magOS...")
            sys.exit(0)
        else:
            print("Unknown command. Type 'help' for a list of commands.")
    #the whole system is based on the commands folder. the main one is not even 50 lines

if __name__ == "__main__":
    main()