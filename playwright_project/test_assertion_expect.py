from playwright.sync_api import sync_playwright,expect
def test_login():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        context=browser.new_context()
        page=context.new_page()

        page.goto("https://www.saucedemo.com/")

        #assertion using expect
        expect(page).to_have_title("Swag Labs")

        #login
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.get_by_role("button",name="Login").click()

        #Assertion using expect

        expect(page).to_have_url( "https://www.saucedemo.com/inventory.html")

        #Check products

        expect(page.get_by_text("Products")).to_be_visible()
        context.close()
        browser.close()