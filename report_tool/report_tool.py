from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchAttributeException
import time
import sys
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
ua = UserAgent()
zz = input("File for login? (leave blank to put manually): ")
if zz:
    file1 = open(zz, "r")

    # Reading line
    for line in file1:
        # username:password splitter
        fieldss = line.split(":")
        username11 = fieldss[0]
        pass22 = fieldss[1]
else:
    pass
    username11 = input("Username?: ")
    pass22 = input("Pass: ")

user_of_data = input("Username to get data? (if you dont want this, leave blank): ")
searchany = input("Want to use the search? (y/n): ")
if username11 == "" or pass22 == "":
    sys.exit("Username or Password empty.")

profile1 = webdriver.FirefoxProfile()
profile1.set_preference("general.useragent.override", ua.random)
driver = webdriver.Firefox(profile1)
agent = driver.execute_script("return navigator.userAgent")


def __init__(self, username11, pass22):
    self.username = username11
    self.password = pass22

def login():
    driver.get("https://www.instagram.com/")
    time.sleep(2)
    login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
    login_button.click()
    time.sleep(2)
    time.sleep(2)
    user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
    user_name_elem.clear()
    user_name_elem.send_keys(username11)
    passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
    passworword_elem.clear()
    passworword_elem.send_keys(pass22)
    passworword_elem.send_keys(Keys.RETURN)
    time.sleep(1.75)

login()
try:
    driver.find_element_by_css_selector(".GNbi9")
    print("")
    print("Suspicious login :(")
    driver.quit()
except NoSuchElementException:
    print("Logged!")

try:
    driver.find_element_by_css_selector(".aOOlW.HoLwm").click()
except NoSuchElementException:
    pass
    time.sleep(1.25)

def get_data(user_of_data):
    driver.get("https://www.instagram.com/" + user_of_data + "/")
    time.sleep(0.5)
    print("")
    a = []
    b = []
    try:
        driver.find_element_by_css_selector(".main.-cx-PRIVATE-Page__main.-cx-PRIVATE-Page__main__")
        print("")
        print("User not found :(")
        print("")
        wwwa99 = input("Try other user? (y/n): ")
        if wwwa99 == "y" or wwwa99 == "Y" or wwwa99 == "yes" or wwwa99 == "Yes":
            asz8 = input("Username to get data? (if you dont want this, leave blank): ")
            if asz8:
                get_data(asz8)
            else:
                pass
    except NoSuchElementException:
        all_spans = driver.find_elements_by_css_selector('.g47SY')
        for span in all_spans:
            b.append(span.get_attribute("title"))
            a.append(span.text)
        time.sleep(0.5)
        if (b[1] == ""):
            b[1] = a[1]
        print(user_of_data + "'s data")
        print("--------------------")
        print(a[0] + " posts")
        print(b[1] + " followers")
        print(a[2] + " following")
        print("--------------------")
        print("")
        wwwa = input("Get another user data? (y/n): ")
        if wwwa == "y" or wwwa == "Y" or wwwa == "yes" or wwwa == "Yes":
            asz = input("Username to get data? (if you dont want this, leave blank): ")
            if asz:
                get_data(asz)
            else:
                pass

if user_of_data:
    get_data(user_of_data)

if (searchany == "y" or searchany == 'Y'):
    data_term = input("User to get photos links (empty if you dont want this): ")
    if (data_term == ""):
        sys.quit("Closed :)")
    driver.get("https://www.instagram.com/" + data_term + "/")
    time.sleep(0.5)
    print("")
    photos_links = []
    all_photos = driver.find_elements_by_css_selector('.FFVAD')
    for pht in all_photos:
        photos_links.append(pht.get_attribute("src"))
    i = 0
    while i < len(photos_links):
        print(photos_links[i])
        i += 1

else:
    pass