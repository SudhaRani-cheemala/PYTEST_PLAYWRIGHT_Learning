from playwright.sync_api import sync_playwright
def test_locators():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto("https://www.saucedemo.com/")
        page.get_by_placeholder("username").fill("standrd_user")
        page.get_by_placeholder("Password").fill("scret_password")
        page.get_by_role("button",name="Login").click()
        browser.close()