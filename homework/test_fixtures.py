"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import os
import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope='function')
def browser_desktop():
    browser.config.window_height = 800
    browser.config.window_width = 1280
    browser.config.base_url = 'https://github.com'
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    yield

    browser.quit()

@pytest.fixture(scope='function')
def browser_mobile():
    browser.config.window_height = 2556
    browser.config.window_width = 1179
    browser.config.base_url = 'https://github.com'
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    yield

    browser.quit()


def test_github_desktop(browser_desktop):
    browser.open()
    browser.element()


def test_github_mobile(browser_mobile):
    pass
