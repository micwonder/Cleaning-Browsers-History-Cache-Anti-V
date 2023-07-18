import selenium.webdriver as webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time
from webdriver_manager.microsoft import EdgeChromiumDriverManager
options = Options()
options.add_argument("--headless=new")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
options.binary_location=R'C:\Program Files (x86)\Microsoft\EdgeCore\114.0.1823.82\msedge.exe'
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
driver.get("edge://settings/clearBrowserData")
driver.fullscreen_window()
try:
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#clear-now"))
    )
except:
    print('Can\'t load clear browsing data page')
try:
    ele = driver.find_element(By.CSS_SELECTOR, '#clear-now')
    ele.click()
except:
    print('Can\'t click the clear now button!')
driver.quit()