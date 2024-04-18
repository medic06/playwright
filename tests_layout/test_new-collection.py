from playwright.sync_api import Playwright, sync_playwright, expect


def test_new_collection(go_to_new_collection) -> None:
    page = go_to_new_collection
    page.get_by_role("link", name="Home").click()
    page.get_by_role("link", name="Shop Women Winter").click()

    all_links = page.get_by_role("link").all()
    for link in all_links:
        if '$85' in link.text_content():
            assert 'socks' not in link.text_content().lower()

# ---------------------
# TODO: Tear down to be handled by conftest.py
# context.close()
# browser.close()

# with sync_playwright() as playwright:
#     test_login(playwright)
