import requests
import zipfile
from art import text2art
from colorama import Fore
from os import system, remove
from time import sleep
from config import DRIVER_PATH, ZIP_PATH

system("cls")
print(Fore.WHITE + text2art("CHROME DRIVER", font='fuzzy'))
print(Fore.LIGHTBLUE_EX + "by luwufka, 2024")
sleep(1)

def download(url):
    print(Fore.LIGHTYELLOW_EX + "[INFO]: Downloading...")
    response = requests.get(url)
    if (response.status_code == 200):
        with open(ZIP_PATH, 'wb') as file:
            file.write(response.content)
        with zipfile.ZipFile(ZIP_PATH, 'r') as zf:
            try:
                if("chromedriver.storage.googleapis.com" in url):
                        print(Fore.LIGHTYELLOW_EX + "[INFO]: Unpacking using the method below v. 115...")
                        zf.extractall(path="")
                else:
                    print(Fore.LIGHTYELLOW_EX + "[INFO]: Unpacking by the method from and above v. 115...")
                    with zf.open('chromedriver-win32/chromedriver.exe') as driver:
                        content = driver.read()
                        with open(DRIVER_PATH, 'wb') as driver_file:
                            driver_file.write(content)
            except Exception as e:
                print(Fore.RED + f"[ERROR]: Could not unpack! Details:\n{Fore.WHITE}{e}")
        try:
            remove(ZIP_PATH)
        except:
            print(Fore.YELLOW + "[WARNING]: Error deleting the zip file!")
        print(Fore.LIGHTGREEN_EX + "[INFO]: Done!")
        print(Fore.WHITE + "[INFO]: Exit the utility...")
        sleep(2)
    else:
        print(Fore.RED + f"[ERROR]: An error has occurred! Code: #{response.status_code}")

version_str = input("Enter the Chrome version (chrome://settings/help): ")
if (int(version_str[:3]) >= 115):
    download(f"https://storage.googleapis.com/chrome-for-testing-public/{version_str}/win32/chromedriver-win32.zip")
else:
    download(f"https://chromedriver.storage.googleapis.com/{version_str}/chromedriver_win32.zip")
exit()