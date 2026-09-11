from playwright.sync_api import sync_playwright,expect
def test_login():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        context=browser.new_context()
        page=context.new_page()
        page.goto("https://www.saucedemo.com/")

        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.get_by_role("button",name="Login").click()

        #Explicitely waits for products

        products=page.get_by_text("Products")
        products.wait_for(
         state="visible",
         timeout=10000         
        )

        #Assertion
        expect(products).to_be_visible()
        context.close()
        browser.close()