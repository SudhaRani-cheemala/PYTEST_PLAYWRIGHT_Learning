from playwright.sync_api import sync_playwright


def test_actions():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        # Enter username
        page.get_by_placeholder("Username").fill("standard_user")

        # Enter password
        page.get_by_placeholder("Password").fill("secret_sauce")

        # Click Login
        page.get_by_role("button", name="Login").click()

        # Hover over Products
        page.get_by_text("Products").hover()

        page.locator("select").select_option("value")

        page.locator("select").select_option(label="India")

        page.locator("#username").press("Enter")
        page.locator("#element").dblclick()

        browser.close()



#         Locator
#    ↓
# Does element exist?
#    ↓
# YES → Action happens ✅
# NO  → Playwright waits → TimeoutError ❌