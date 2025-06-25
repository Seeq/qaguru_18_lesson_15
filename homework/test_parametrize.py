import pytest
from selene import browser, have


@pytest.fixture(params=[(1920, 1080), (1280, 1024), (375, 665), (430, 932)], ids=["1920x180", "1280x1024","375x665","430x932"])
def browser_config(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()

@pytest.mark.parametrize("browser_config",[(1920, 1080), (1280, 1024)],ids=["1920x1080", "1280x1024"],indirect=True)
def test_github_desktop(browser_config):
    browser.open("https://github.com/")
    browser.all('button').element_by(have.text('Sign up')).click()

@pytest.mark.parametrize("browser_config",[(375, 665), (430, 932)],ids=["375x665", "430x932"],indirect=True)
def test_github_mobile(browser_config):
    browser.open("https://github.com/")
    browser.element('.Button-content').click()
    browser.element('.HeaderMenu-link--sign-up').click()
