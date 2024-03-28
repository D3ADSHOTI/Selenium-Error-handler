from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import threading
import pyautogui
import schedule
import time


# Import other necessary modules like Selenium, pyautogui, etc.

def example():
    options = Options()
    options.add_experimental_option("detach", True)

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    driver.get("https://example.com")
    driver.set_window_position(750, 0)
    driver.set_window_size(750, 512)

    while True:
        e = driver.find_elements(By.XPATH, "/html/body/div/div[3]/div/button")  # Go in inspect element on Chrome or firefox, select the element (ctrl+shift+c) you want to copy then click "Copy full xpath" then paste in driver.find_elements section.
        if not e:
            print("Element not found 1")
            time.sleep(100)
            pyautogui.moveTo(98, 59)
            time.sleep(1)
            pyautogui.click()


def example2():
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=options)

    driver.get("https://example.com")
    driver.set_window_position(0, 0)
    driver.set_window_size(750, 512)

    while True:
        e = driver.find_elements(By.XPATH, "/html/body/div/div[3]/div/button")  # Go in inspect element on Chrome or firefox, select the element (ctrl+shift+c) you want to copy then click "Copy full xpath" then paste in driver.find_elements section.
        if not e:
            print("Element not found 2")
            time.sleep(100)
            pyautogui.moveTo(850, 57)
            time.sleep(1)
            pyautogui.click()


def example3():
    options = Options()
    options.add_experimental_option("detach", True)

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    driver.get("https://example.com")
    driver.set_window_position(750, 535)
    driver.set_window_size(750, 512)

    while True:
        e = driver.find_elements(By.XPATH, "/html/body/div/div[3]/div/button")  # Go in inspect element on Chrome or firefox, select the element (ctrl+shift+c) you want to copy then click "Copy full xpath" then paste in driver.find_elements section.
        if not e:
            print("Element not found 3")
            time.sleep(100)
            pyautogui.moveTo(101, 594)
            time.sleep(1)
            pyautogui.click()


def example4():
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=options)

    driver.get("https://example.com")
    driver.set_window_position(0, 535)
    driver.set_window_size(750, 512)

    while True:
        e = driver.find_elements(By.XPATH, "/html/body/div/div[3]/div/button")  # Go in inspect element on Chrome or firefox, select the element (ctrl+shift+c) you want to copy then click "Copy full xpath" then paste in driver.find_elements section.
        if not e:
            print("Element not found 4")
            time.sleep(100)
            pyautogui.moveTo(851, 595)
            time.sleep(1)
            pyautogui.click()


def coding():
    pyautogui.moveTo(433, 321)
    time.sleep(5)

    pyautogui.moveTo(1093, 295)
    time.sleep(5)

    time.sleep(0.5)
    pyautogui.moveTo(294, 1008)
    time.sleep(5)

    pyautogui.moveTo(941, 1007)
    time.sleep(5)


# Run the example functions in their threads
example_thread = threading.Thread(target=example)
example2_thread = threading.Thread(target=example2)
example3_thread = threading.Thread(target=example3)
example4_thread = threading.Thread(target=example4)

example_thread.start()
example2_thread.start()
example3_thread.start()
example4_thread.start()


# Time
#schedule.every(1).seconds.do(coding) # You could let this code run with other code while threading runs in the background.

# This is disabled because threading has a target set, remove (target=example) on line 118 to schedule, same goes for the schedules below.
#schedule.every().day.at("00:00").do(example)
#schedule.every().day.at("01:00").do(example2)
#schedule.every().day.at("02:00").do(example3)
#schedule.every().day.at("03:00").do(example4)

while True:
    schedule.run_pending()
    time.sleep(1)