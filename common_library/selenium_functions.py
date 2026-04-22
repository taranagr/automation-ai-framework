import os

from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def open_browser(browser_name="chrome"):
    chrome_options = Options()
    chrome_options.add_argument("--log-level=1")
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("start-maximized")
    if os.environ["HEALENIUM_FLAG"] == "YES":
        node_url = "http://localhost:8085/"
        driver = webdriver.Remote(
            command_executor=node_url,
            options=chrome_options,
        )
    else:
        driver = webdriver.Chrome(options=chrome_options)
    driver.delete_all_cookies()
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver