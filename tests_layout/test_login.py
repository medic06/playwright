from playwright.sync_api import Playwright, sync_playwright, expect
import os

PASSWORD = os.environ['PASSWORD']

def test_login(set_up_1) -> None:
    # Access main page for login
    page = set_up_1
    page.wait_for_load_state("networkidle")

# Steps to login with email ---> moved to conftest.py login fixture
#     page.get_by_role("button", name="Log In").click()
#     page.get_by_test_id("signUp.switchToSignUp").click()
#     page.get_by_role("button", name="Log in with Email").click()
#     page.get_by_test_id("emailAuth").get_by_label("Email").click()
#     page.get_by_test_id("emailAuth").get_by_label("Email").fill("imedic06@gmail.com")
#     page.get_by_test_id("emailAuth").get_by_label("Email").press("Tab")
#     page.get_by_label("Password").fill(PASSWORD)
#     page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
#     page.wait_for_load_state("networkidle")

# Check if login was successful
    # page.pause()
    expect(page.locator("[aria-label=\"imedic06 account menu\"]")).to_be_visible()
    expect(page.get_by_role("button", name="Log In")).to_be_hidden()
    expect(page.get_by_text(".cls-anonymous-icon{fill: inherit}imedic06")).to_be_visible()

    print("Exit code 0 means success")

    # ---------------------
    # context.close()
    # browser.close()


# with sync_playwright() as playwright:
#     test_login(playwright)
