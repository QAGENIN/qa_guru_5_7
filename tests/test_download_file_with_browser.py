import os
import time
from selenium import webdriver
from selene import browser
from zipfile import ZipFile
from conftest import PROJECT_TMP_PATH


# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp

def test_browser_download_file():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": PROJECT_TMP_PATH,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)

    browser.config.driver_options = options

    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()

    assert os.path.exists(os.path.join(PROJECT_TMP_PATH, 'pytest-main.zip'))
    assert os.path.getsize(os.path.join(PROJECT_TMP_PATH, 'pytest-main.zip')) > 0
