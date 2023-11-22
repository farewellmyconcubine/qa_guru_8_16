"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, have


@pytest.fixture(params=['desktop', 'mobile'])
def browser_setup(request):
    if request.param == 'desktop':
        browser.config.window_width = 1920
        browser.config.window_height = 1080

    if request.param == 'mobile':
        browser.config.window_width = 414
        browser.config.window_height = 896

    yield

    browser.quit()


@pytest.mark.parametrize("browser_setup", ['desktop'], indirect=True)
def test_github_desktop(browser_setup):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize("browser_setup", ['mobile'], indirect=True)
def test_github_mobile(browser_setup):
    browser.open('https://github.com/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
