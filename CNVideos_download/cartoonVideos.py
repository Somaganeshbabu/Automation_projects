import time
import pyautogui
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
chrome_options = Options()
options = webdriver.ChromeOptions()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options.add_experimental_option("detach", True)

class cartoonDownloadUsingXpath():
    def locatingUrl(self):
        driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.wcofun.net/anime/power-rangers-mystic-force")  # -- paste any url mentioned in PowerRangersUrl.txt file --
        list_of_Videos = driver.find_elements("xpath","//div[@id='sidebar_right3']//div")
        length = len(list_of_Videos)
        time.sleep(5)
        for links in range(1,length):
             driver.find_elements("xpath","//div[@id='sidebar_right3']//div[%d]" %(links))[0].click()
             driver.execute_script("window.scrollBy(0,500)")
             driver.find_element("xpath", "//iframe[@id='cizgi-js-0']").click()
             time.sleep(7)                            # -------- to Play the video -------
             print(pyautogui.size())
             pyautogui.moveTo(960,540)
             #-- video located position---
             pyautogui.click(button = 'right')
             time.sleep(5)
             pyautogui.press('down',4)                # -- Moving to 4th option which is saveAs-----
             pyautogui.press('enter')
             time.sleep(10)                           # -- if u need to locate where to download ----
             driver.back()
findlistUrl = cartoonDownloadUsingXpath()
findlistUrl.locatingUrl()