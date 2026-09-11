from playwright.sync_api import sync_playwright


def test_new_context():

    with sync_playwright() as p:

        # Start browser
        browser = p.chromium.launch(headless=False)

        # Create browser context
        context = browser.new_context()

        # Create page inside the context
        page = context.new_page()

        # Open website
        page.goto("https://www.saucedemo.com/")

        print("Page title:", page.title())

        # Login
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.get_by_role("button", name="Login").click()

        # Print current URL
        print("Current URL:", page.url)

        # Close context
        context.close()

        # Close browser
        browser.close()


#         4. Interview question

# Q: Why do we use browser.new_context()?

# You can answer:

# browser.new_context() creates an isolated browser session. Each context has its own cookies, local storage, and session data. We can use multiple contexts to test different users or independent sessions within the same browser.