import os
import selenium.webdriver as webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
def clear_msedge_data():
    options = EdgeOptions()
    options.add_argument("--headless=new")
    options.binary_location = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    try:
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
    except:
        print('\nCan\'t find the msedge.exe')
    driver.get("edge://settings/clearBrowserData")
    driver.fullscreen_window()
    try:
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#clear-now")))
    except:
        print('\nCan\'t load clear browsing Microsoft Edge page')
        driver.quit()
        return
    try:
        clear_now_button = driver.find_element(By.CSS_SELECTOR, '#clear-now')
        clear_now_button.click()
    except:
        print('\nCan\'t click the clear now button on Microsoft Edge.')
        driver.quit()
        return
        time.sleep(5)  # Wait for the clearing process to complete
    driver.quit()
    print('\nCleared browsing data in Microsoft Edge successfully.')
def clear_firefox_data():
    # Create a Firefox profile
    profile = FirefoxProfile()
    # Set the profile preferences to clear data on startup
    profile.set_preference("browser.privatebrowsing.autostart", True)
    profile.set_preference("privacy.clearOnShutdown.cache", True)
    profile.set_preference("privacy.clearOnShutdown.cookies", True)
    profile.set_preference("privacy.clearOnShutdown.downloads", True)
    profile.set_preference("privacy.clearOnShutdown.formdata", True)
    profile.set_preference("privacy.clearOnShutdown.history", True)
    profile.set_preference("privacy.clearOnShutdown.offlineApps", True)
    profile.set_preference("privacy.clearOnShutdown.sessions", True)
    profile.set_preference("privacy.clearOnShutdown.siteSettings", True)
    # Set additional preferences to clear data immediately
    profile.set_preference("privacy.cpd.cache", True)
    profile.set_preference("privacy.cpd.cookies", True)
    profile.set_preference("privacy.cpd.formdata", True)
    profile.set_preference("privacy.cpd.history", True)
    profile.set_preference("privacy.cpd.offlineApps", True)
    profile.set_preference("privacy.cpd.passwords", True)
    profile.set_preference("privacy.cpd.siteSettings", True)
    # Set the path to the Firefox executable (change if necessary)
    firefox_path = r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'
    # Configure Firefox options
    options = FirefoxOptions()
    options.binary_location = firefox_path
    options.add_argument('--headless=new')
    options.profile = profile
    # Create the Firefox webdriver instance with the specified profile and options
    # driver = webdriver.Firefox(firefox_profile=profile, options=options)
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    # Open any URL to trigger data clearing
    driver.get("about:blank")
    # Close the webdriver
    driver.quit()
    print('\nCleared browsing data in Firefox successfully.')
def flush_dns_cache():
    os.system("ipconfig /flushdns")
def run():
    clear_msedge_data()
    clear_firefox_data()
    flush_dns_cache()
if __name__ == "__main__":
    run()