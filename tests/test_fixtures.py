"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser, have


@pytest.fixture
def desktop_setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()


@pytest.fixture
def mobile_setup():
    browser.config.window_width = 414
    browser.config.window_height = 896

    yield

    browser.quit()


def test_github_desktop(desktop_setup):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_github_mobile(mobile_setup):
    browser.open('https://github.com/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
