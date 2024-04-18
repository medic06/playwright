import pytest
from playwright.sync_api import expect

#TODO: Develop better negative tests for login
@pytest.mark.skip(reason="tests fail intentionally need to find a better way to do this")
@pytest.mark.parametrize("email, password", [("", ""),
                                               ("imedic06@gmail", "P@$$w0rd"),
                                               ("imedic06@gmail.com", "Password")])
def test_login_param_neg_tests(set_up_1, email, password) -> None:
    # Access main page for login
    page = set_up_1
    page.wait_for_load_state("networkidle")

    # Steps to login with email
    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill(email)
    page.get_by_test_id("emailAuth").get_by_label("Email").press("Tab")
    page.get_by_label("Password").fill(password)
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    page.wait_for_load_state("networkidle")

    # Check if login was successful
    # page.pause()
    expect(page.locator("[aria-label=\"imedic06 account menu\"]")).to_be_visible()
    expect(page.get_by_role("button", name="Log In")).to_be_hidden()
    expect(page.locator("text=Celebrating Beauty and Style")).to_be_visible()

    print("Exit code 0 means success")
