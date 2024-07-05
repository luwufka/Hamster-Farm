# ![hamster-x32](https://github.com/luwufka/Hamster-Farm/assets/126056242/fe510c02-aad7-4553-9b93-9d469561c6f5) Hamster Farm
Automatic reward collection in Hamster Kombat.
> made for fun. but it really works :0

## Manual:
> Telegram login data and API keys are not required to be entered.

> You need to get a URL. But how?
### 🐹 How do I get the URL?
1. Log in to Telegram Web (Use Version A)!
   
![image](https://github.com/luwufka/Hamster-Farm/assets/126056242/3817f13d-0698-4562-9205-5841f9f0ee5f)
3. Start the game in the official Hamster Kombat bot. Even if you received a message that you need to log in from your phone, it's okay.
4. At this time, run this script in the browser console: `document.querySelector('iframe[title^=Hamster]').src`
![image](https://github.com/luwufka/Hamster-Farm/assets/126056242/9ff8e504-c883-4fa2-a0bd-dab2b4cde32d)
6. You get a very long link at the output. In the link, set the value **tgWebAppVersion** to **ios** (you can use another option, but not the fact that some will work): ![image](https://github.com/luwufka/Hamster-Farm/assets/126056242/a5c194de-2367-4cb8-b9fb-2750217659b8)

7. Add the modified URL to the **URLS** array. *Array of URLs in the file **config.py**.*

   
*p.s. you can use multiple links and add them to the array to farm on multiple accounts...*
### ⚙️ Installation and launch:
*After you have set up **config.py** let's start the installation and launch.*
1. Install all libraries from **requirements.txt**.
2. Launch **main.py**.
> If the driver is not installed, the script will install it itself. But...
1. Copy the Google Chrome version by URL: `chrome://settings/help`
2. Enter it **without extra spaces and characters!**
3. At the end of the installation, the script will be closed, and the file **chromedriver.exe** it should appear in the directory with the script.
4. Run **main.py** again.

> Good Luck!
