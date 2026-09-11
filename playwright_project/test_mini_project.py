from playwright.sync_api import sync_playwright,expect
def test_mini_project():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        context=browser.new_context()
        page=context.new_page()
        page.goto("https://www.saucedemo.com/")

        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.get_by_role("Button",name="Login").click()

        #Expect
        expect(page.get_by_text("Products")).to_be_visible()
        context.close()
        browser.close()

from playwright.sync_api import sync_playwright, expect

def test_add_products():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.saucedemo.com/")

        # Login
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.get_by_role("button", name="Login").click()

        # Add product
        page.get_by_role("button", name="Add to cart").first.click()

        # Open cart
        page.locator(".shopping_cart_link").click()

        # Verify cart
        expect(page.get_by_text("Your Cart")).to_be_visible()

        context.close()
        browser.close()


def test_product_in_cart():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        context = browser.new_context()

        page = context.new_page()

        page.goto("https://www.saucedemo.com/")

        # Login
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.get_by_role("button", name="Login").click()

        # Add backpack
        page.get_by_role(
            "button",
            name="Add to cart"
        ).first.click()

        # Go to cart
        page.locator(".shopping_cart_link").click()

        # Verify product
        expect(
            page.get_by_text("Sauce Labs Backpack")
        ).to_be_visible()

        context.close()
        browser.close()        