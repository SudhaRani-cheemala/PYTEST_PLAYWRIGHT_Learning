from playwright.sync_api import sync_playwright


def test_checkbox():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        context = browser.new_context()

        page = context.new_page()

        page.goto("https://the-internet.herokuapp.com/checkboxes")

        # Check first checkbox
        page.locator("input[type='checkbox']").nth(0).check()

        # Check second checkbox
        page.locator("input[type='checkbox']").nth(1).check()

        context.close()
        browser.close()