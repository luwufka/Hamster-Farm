from art import text2art
from os import system, path
from time import sleep
from colorama import Fore
from config import DRIVER_PATH, URLS, GETREWARD_COOLDOWN_SEC

system("cls")
print(Fore.WHITE + text2art("HAMSTER FARM", font='bulbhead'))
version = "v. 1.0.0"
print(Fore.LIGHTBLUE_EX + f"by luwufka, 2024 {Fore.WHITE}[{version}]")
sleep(1)

if (not path.exists(DRIVER_PATH)):
    print(Fore.YELLOW + "[WARNING]: ChromeDriver has not been detected!\nNow it will be installed (you need to restart the script after installing the driver).")
    sleep(2)
    import chromedriver
else:
    print(Fore.YELLOW + "[WARNING]: Please set the time and URL in *config.py*\n(For more information on GitHub -> luwufka/Hamster-Farm)")
    sleep(1)
    import tools
    while True:
        tools.get_reward(URLS)
        print(Fore.LIGHTYELLOW_EX + "[INFO]: Completed! We're waiting...")
        sleep(GETREWARD_COOLDOWN_SEC)