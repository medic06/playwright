import os
import time

import pytest
from playwright.sync_api import Playwright

PASSWORD = os.environ['PASSWORD']


@pytest.fixture(scope="session")
def context_creation(playwright: Playwright):
    # From here to ...
    browser = playwright.chromium.launch(headless=False)
    # browser = playwright.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context()
    page = context.new_page()
    # To here can be removed if using built-in page fixture < def set_up(page): > (deffaults to headless=true) CLI commands
    # can be used instead to run tests with different params
    # ie playwright test --headed --browser=chromium --browser=firefox --browser=webkit ... ect.
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    # page.pause()

    page.wait_for_load_state("networkidle")

    # login_issue = True
    # while login_issue:
    #     if not page.is_visible("[data-test-id=\"signUp.switchToSignUp\"]"):
    #         page.click("button:has-text(\"Log In\")")
    #     else:
    #         login_issue = False
    #     time.sleep(0.1)
    page.get_by_text("Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("imedic06@gmail.com")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("Tab")
    page.get_by_label("Password").fill(PASSWORD)
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    page.wait_for_load_state("networkidle")
    context.storage_state(path="state.json")

    yield context
    # page.close()


@pytest.fixture
def set_up_1(context_creation):
    context = context_creation
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")

    yield page
    page.close()


@pytest.fixture
def go_to_new_collection(set_up_1):
    page = set_up_1
    page.goto("https://symonstorozhenko.wixsite.com/website-1/new-collection")
    page.wait_for_load_state("networkidle")

    yield page
    page.close()
