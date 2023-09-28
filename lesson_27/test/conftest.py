import time

import pytest
from selenium import webdriver
from hillel_aqa_050623.lesson_27.pages.main_page import MainPage

USERNAME = 'guest'
PASSWORD = 'welcome2qauto'
URL = 'qauto.forstudy.space'


@pytest.fixture(scope='session')
def open_students_site():
    driver = webdriver.Firefox()
    try:
        driver.get(f'https://{USERNAME}:{PASSWORD}@{URL}')
        yield driver
    finally:
        driver.quit()
    time.sleep(5)
