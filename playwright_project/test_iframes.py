from playwright.sync_api import sync_playwright

def test_iframe():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(
            "https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe"
        )

        frame = page.frame_locator('iframe[name="iframeResult"]')

        frame.locator("body").wait_for(state="visible")

        print("Iframe found successfully")

        browser.close()