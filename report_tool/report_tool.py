from selenium import webdriver
import time
from fake_useragent import UserAgent
from selenium.common.exceptions import ElementNotInteractableException
ua = UserAgent()
#list = open("ips.txt").readlines()
# ip = random.choice((list))
# print(ip)
#
# myProxy = ip
#
# webdriver.DesiredCapabilities.FIREFOX['proxy']={
#  "httpProxy":myProxy,
#  "ftpProxy":myProxy,
#  "sslProxy":myProxy,
#  "proxyType":"MANUAL"
# }
try:
    while True:
        s1 = input("Username?: ")
        s2 = input("Real Name?: ")
        s3 = input("Day?: ")
        s4 = input("Month?: ")
        s5 = input("Year?: ")
        profile1 = webdriver.FirefoxProfile()
        profile1.set_preference("general.useragent.override", ua.random)
        driver = webdriver.Firefox(profile1)
        agent = driver.execute_script("return navigator.userAgent")
        driver.get('https://help.instagram.com/contact/723586364339719')
        username = driver.find_element_by_id('258021274378282')
        time.sleep(1.25)
        username.send_keys(s1)
        real = driver.find_element_by_id('735407019826414')
        time.sleep(1.5)
        real.send_keys(s2)
        year = driver.find_element_by_xpath("//select[@class='periodMenu yearMenu']/option[@value='" + s5 + "']").click()
        time.sleep(1.75)
        month = driver.find_element_by_xpath("//select[@data-name='month']/option[@value='" + s4 + "']").click()
        time.sleep(1.85)
        day = driver.find_element_by_xpath("//select[@data-name='day']/option[@value='" + s3 + "']").click()
        time.sleep(1.75)
        relation = driver.find_element_by_xpath("//select[@id='294540267362199']/option[@value='Other']").click()
        time.sleep(3)
        button = driver.find_element_by_css_selector('._4jy1').click()
        driver.implicitly_wait(10)
        emnt = driver.find_element_by_css_selector('._42g-').click()
        driver.quit()
        print("")
        print("Reported!")
        print("-------------------------------")
        print("Username Reported: " + s1)
        print("Real Name: " + s2)
        print("Date Submited: " + s3 + "/" + s4 + "/" + s5)
        print("-------------------------------")
        print("")
        while True:
            answer = input('Run again? (y/n): ')
            if answer in ('y', 'n'):
                break
            print("Invalid input.")
        if answer == 'y':
            print("")
            continue
        else:
            print("")
            print('Exited.')
            break
except ElementNotInteractableException:
    print("Page not loaded correctly, sometimes happens, please try again.")

