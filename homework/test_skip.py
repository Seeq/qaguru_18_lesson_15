import pytest
from selene import browser, have


@pytest.fixture(params=[(1920, 1080), (1280, 1024), (375, 665), (430, 932)],
                ids=["1920x180", "1280x1024", "375x665", "430x932"])
def browser_config(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if width <= 430:
        yield "mobile"
        browser.quit()
    else:
        yield "desktop"
        browser.quit()


def test_github_desktop(browser_config):
    if browser_config == "mobile":
        pytest.skip(reason="screen resolution for mobile devices")
    browser.open("https://github.com/")
    browser.all('button').element_by(have.text('Sign up')).click()


def test_github_mobile(browser_config):
    if browser_config == "desktop":
        pytest.skip(reason="Desktop screen resolution")
    browser.open("https://github.com/")
    browser.element('.Button-content').click()
    browser.element('.HeaderMenu-link--sign-up').click()
