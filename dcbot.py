from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import os

tc = input("Trade Central disabled? (y/n):  ")

a = os.path.abspath(__file__)
a = a[:-8]
b = a+"chromedriver.exe"
c = a+"itemlist.txt"
f = a+"config.txt"
g = []

with open(f,"r",encoding="utf-8") as file:
    for x in file:
        g.append(x.strip("\n"))

id = g[0]
passwordd = g[1]
cooldown = g[2]
cooldown = cooldown[21:]
cooldown = int(cooldown)

option = webdriver.ChromeOptions()
option.add_argument("--headless")
option.add_argument("--disable-gpu")
option.add_argument("--log-level=3")

browser = webdriver.Chrome(b,options=option)
browser.get("https://discord.com/login")
time.sleep(5)

username = browser.find_element_by_xpath("//*[@id='app-mount']/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/input")
password = browser.find_element_by_xpath("//*[@id='app-mount']/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input")

username.send_keys(id[3:])
time.sleep(1)
password.send_keys(passwordd[9:])
time.sleep(1)
webdriver.ActionChains(browser).send_keys(Keys.ENTER).perform()
print("Logged in to Discord.")
time.sleep(8)

while True:
    d = []
    with open(c,"r",encoding="utf-8") as file2:
        for i in file2:
            d.append(i.strip("\n"))
    browser.get("https://discord.com/channels/152517096104919042/239085283616882688")
    time.sleep(5)
    sayi = 0
    for j in d:
        webdriver.ActionChains(browser).send_keys(j).perform()
        webdriver.ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
        sayi = sayi + 1
        if sayi == 4:
            break    
    webdriver.ActionChains(browser).send_keys(Keys.ENTER).perform()
    print("Posted in Rocket League")
    time.sleep(1)
    browser.get("https://discord.com/channels/247628906914512896/249642821047418881")
    time.sleep(5)
    sayi = 0
    for j in d:
        webdriver.ActionChains(browser).send_keys(j).perform()
        webdriver.ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
        sayi = sayi + 1
        if sayi == 15:
            break    
    webdriver.ActionChains(browser).send_keys(Keys.ENTER).perform()
    print("Posted in Rocket Planet")
    time.sleep(1)
    if not tc == "y" and not tc == "Y":
        browser.get("https://discord.com/channels/223259649967652887/565265964799623177")
        time.sleep(5)
        sayi = 0
        for j in d:
            webdriver.ActionChains(browser).send_keys(j).perform()
            webdriver.ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
            sayi = sayi + 1
            if sayi == 8:
                break    
        webdriver.ActionChains(browser).send_keys(Keys.ENTER).perform()
        print("Posted in Trade Central")
        time.sleep(1)
    browser.get("https://discord.com/channels/280753127043497987/280753307860074496")
    time.sleep(5)
    sayi = 0
    for j in d:
        webdriver.ActionChains(browser).send_keys(j).perform()
        webdriver.ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
        sayi = sayi + 1
        if sayi == 15:
            break    
    webdriver.ActionChains(browser).send_keys(Keys.ENTER).perform()
    print("Posted in Rocket League Garage")
    time.sleep(1)
    browser.get("https://discord.com/channels/346755536747757569/363460545006796800")
    time.sleep(5)
    sayi = 0
    for j in d:
        webdriver.ActionChains(browser).send_keys(j).perform()
        webdriver.ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
        sayi = sayi + 1
        if sayi == 20:
            break    
    webdriver.ActionChains(browser).send_keys(Keys.ENTER).perform()
    print("Posted in RL Insider")
    print("*****************************************************************")
    print("Posted in all the channels.Waiting for {} minutes to start again.".format(cooldown))
    time.sleep(cooldown*60)






