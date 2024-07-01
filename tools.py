from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from config import DRIVER_PATH, JS_GETREWARDBUTTON, JS_GETREWARDVALUE, JS_REWARDBUTTON_ISLOADING
from time import sleep
from colorama import Fore

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('--log-level=3')

service = Service(DRIVER_PATH)

def get_reward(urls):
    i = 1
    for url in urls:
        print(Fore.WHITE + "============================")
        print(Fore.CYAN + f"[INFO]: The reward has started for URL #{i}...")
        print(Fore.WHITE + "[INFO]: Launching Chrome...")
        chrome = webdriver.Chrome(service=service, options=chrome_options)
        chrome.get(url)
        print(Fore.WHITE + "[INFO]: Loading the Hamster Combat page...")
        while True:
            if (chrome.execute_script(JS_REWARDBUTTON_ISLOADING) == True):
                print(Fore.MAGENTA + "[INFO]: Getting a reward...")
                chrome.execute_script(JS_GETREWARDBUTTON)
                reward_value = chrome.execute_script(JS_GETREWARDVALUE)
                print(Fore.LIGHTGREEN_EX + f"[INFO]: Successfully! You took it away: {reward_value}")
                chrome.quit()
                print(Fore.WHITE + "[INFO]: Quitting a Chrome...")
                return True
            else:
                sleep(0.4)