from playwright.sync_api import sync_playwright

def test_mul_tab():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        context = browser.new_context()

        page = context.new_page()

        page.goto("https://example.com")

        print("Main page:", page.url)

        with context.expect_page() as page_info:
            page.get_by_role("link", name="More information...").click()

        new_page = page_info.value

        new_page.wait_for_load_state()

        print("New page:", new_page.url)
        print("New page title:", new_page.title())

        browser.close()



#         "How do you handle multiple tabs in Playwright?"

# You can answer:

# In Playwright, each browser tab is represented by a Page object. When an action opens a new tab, we can use context.expect_page() to capture the newly opened page. We then use the returned Page object to interact with the new tab. We can also use context.pages to get all open pages in the browser context.

# That's a good interview answer for your level.