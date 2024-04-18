from playwright.sync_api import Playwright, sync_playwright, expect
from POM.home_page_elements import HomePage
import pytest


def test_about_us_section_verbiage(set_up_1) -> None:
    page = set_up_1
    home_page = HomePage(page)

    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()



print("Exit code 0 means success")

# with sync_playwright() as playwright:
#     test_about_us_section_verbiage(playwright) -- Not needed when using pytest

# ---------------------
# TODO: Tear down to be handled by conftest.py
# context.close()
# browser.close()


# with sync_playwright() as playwright:
#     test_login(playwright)
