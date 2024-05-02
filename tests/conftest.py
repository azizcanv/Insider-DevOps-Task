import json
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from webdriver_manager.firefox import GeckoDriverManager
from pages.main import MainPage
from pages.careers import CareersPage
from pages.job import JobPage

@pytest.fixture(scope='session')
def config():
    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)
    assert config['browser'] in ['Firefox', 'Chrome','Headless Chrome']

    return config

@pytest.fixture
def browser(config):
    driver = None
    try:
        if config['browser'] == 'Firefox':
            options = FirefoxOptions()
            options.add_argument('--disable-notifications')
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            driver = webdriver.Firefox(options=options)
        elif config['browser'] == 'Chrome':
            options = ChromeOptions()
            options.add_argument('--disable-notifications')
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            driver = webdriver.Chrome(options=options)
        elif config['browser'] == 'Headless Chrome':
            options = ChromeOptions()
            options.add_argument('--disable-notifications')
            options.add_argument('--headless')
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            driver = webdriver.Chrome(options=options)
        else:
            raise Exception(f'Browser "{config["browser"]}" is not supported')

        # Implicit wait should be applied after driver initialization
        driver.implicitly_wait(10)
        driver.set_window_size(1920, 1080)
        yield driver
    finally:
        if driver is not None:
            driver.quit()

@pytest.fixture
def main_page(browser, config):
    return MainPage(browser, config)

@pytest.fixture
def careers_page(browser):
    return CareersPage(browser)

@pytest.fixture
def job_page(browser, config):
    return JobPage(browser, config)
