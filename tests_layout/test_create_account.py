import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


@pytest.mark.skip(reason="test wont run, captcha is required")
def test_create_account(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Log In").click()
    page.get_by_role("button", name="Sign up with email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("imedic06@gmail.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("P@$$w0rd")
    page.frame_locator("iframe[name=\"a-dc0hpdnnrl9v\"]").get_by_label("I'm not a robot").click()
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    page.get_by_label("imedic06 account menu").click()
    page.get_by_text("Log Out").click()

    # ---------------------
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     test_create_account(playwright)
