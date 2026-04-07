if __name__ != "__main__":
    import os
    import sys

    # Get the parent directory (API library folder)
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    commands_dir = os.path.join(parent_dir, "commands")

    avalible_cmmds = os.listdir(commands_dir)
    avalible_cmmds = [cmd.replace(".py", "") for cmd in avalible_cmmds if cmd.endswith(".py")]
    print("Available commands:")
    for cmd in sorted(avalible_cmmds):
        print(f"  - {cmd}")
else:
    print("Please run this command from the main magOS file. and not directly.")