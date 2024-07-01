#Farm Config:
URLS = []
GETREWARD_COOLDOWN_SEC = 3600 * 3

#Scripts Config:
DRIVER_PATH = "chromedriver.exe"
ZIP_PATH = 'chromedriver-win32.zip'
JS_GETREWARDBUTTON = "document.querySelector('.bottom-sheet-button.button.button-primary.button-large').click();"
JS_GETREWARDVALUE = "return Array.from(document.querySelectorAll('.bs-passive-inner .price-value'), element => element.textContent.trim()).join(', ');"
JS_REWARDBUTTON_ISLOADING = "return document.querySelector('.bottom-sheet-button.button.button-primary.button-large') !== null;"