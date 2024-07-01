# ![hamster-x32](https://github.com/luwufka/Hamster-Farm/assets/126056242/fe510c02-aad7-4553-9b93-9d469561c6f5) Hamster Farm
Automatic reward collection in Hamster Kombat.
> made for fun. but it really works :0

## Manual:
> Telegram login data and API keys are not required to be entered.

> You need to get a URL. But how?
### 🐹 How do I get the URL?
1. Log in to Telegram Web.
2. Start the game in the official Hamster Kombat bot. Even if you received a message that you need to log in from your phone, it's okay.
3. At this time, run this script in the browser console: `document.querySelector('iframe[title^=Hamster]').src`
![image](https://github.com/luwufka/Hamster-Farm/assets/126056242/9ff8e504-c883-4fa2-a0bd-dab2b4cde32d)
5. You get a very long link at the output. You must add this link to the array of **URLS** in **config.py**
   
*p.s. you can use multiple links and add them to the array to farm on multiple accounts...*
### ⚙️ Installation and launch:
*After you have set up config.py let's start the installation and launch.*
1. Install all components from **requirements.txt**.
2. Launch **main.py**.

*If you don't have chromedriver.exe it will be installed automatically. You just need to enter the Chrome version without extra spaces, etc.*

After installation, the script will be closed and you need to run **main.py** again.

## If everything is done correctly, the script will automatically use Selenium and ChromeDriver to collect the reward (which accumulated while you were not in the game).
good luck :3
