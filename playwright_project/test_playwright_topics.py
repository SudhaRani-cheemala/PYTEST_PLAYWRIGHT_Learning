from playwright.sync_api import sync_playwright


def test_playwright_topics():

    # --------------------------------------------------
    # 14 & 15. BROWSER TYPE + HEADED/HEADLESS
    # --------------------------------------------------

    with sync_playwright() as p:

        # Chromium browser
        # headless=False means browser will be visible
        browser = p.chromium.launch(headless=False)

        # --------------------------------------------------
        # 10. BROWSER CONTEXT
        # --------------------------------------------------

        # Create an isolated browser session
        context = browser.new_context()

        # Create a page/tab
        page = context.new_page()

        # Open practice website
        page.goto("https://www.w3schools.com/html/html_forms.asp")

        print("Page title:", page.title())
        print("Page URL:", page.url)

        # --------------------------------------------------
        # 1. MOUSE ACTION - CLICK
        # --------------------------------------------------

        # Click an element
        # Syntax:
        # page.locator("locator").click()

        # Example:
        page.locator("input[name='fname']").click()

        # --------------------------------------------------
        # 2. KEYBOARD ACTION
        # --------------------------------------------------

        # Fill text
        page.locator("input[name='fname']").fill("Dimple")

        # Press a keyboard key
        # Syntax:
        # locator.press("key")

        page.locator("input[name='fname']").press("Control+A")

        # Press Escape
        page.keyboard.press("Escape")

        # --------------------------------------------------
        # MOUSE - HOVER
        # --------------------------------------------------

        # Syntax:
        # locator.hover()

        page.locator("body").hover()

        # --------------------------------------------------
        # MOUSE - DOUBLE CLICK
        # --------------------------------------------------

        # Syntax:
        # locator.dblclick()

        page.locator("input[name='fname']").dblclick()

        # --------------------------------------------------
        # MOUSE - RIGHT CLICK
        # --------------------------------------------------

        # Syntax:
        # locator.click(button="right")

        page.locator("input[name='fname']").click(button="right")

        # --------------------------------------------------
        # 13. SCREENSHOT
        # --------------------------------------------------

        # Take screenshot
        # Syntax:
        # page.screenshot(path="filename.png")

        page.screenshot(path="homepage.png")

        # Full page screenshot
        page.screenshot(
            path="fullpage.png",
            full_page=True
        )

        # --------------------------------------------------
        # 11. TABLE
        # --------------------------------------------------

        # Count rows in a table
        # Syntax:
        # locator.count()

        rows = page.locator("table tbody tr")

        print("Number of rows:", rows.count())

        # Get first row
        if rows.count() > 0:
            print("First row:", rows.nth(0).inner_text())

        # --------------------------------------------------
        # 12. DYNAMIC ELEMENTS
        # --------------------------------------------------

        # Prefer stable locators such as:
        #
        # get_by_role()
        # get_by_text()
        # get_by_label()
        # get_by_placeholder()
        #
        # instead of fragile XPath.

        # Example:
        first_name = page.locator("input[name='fname']")

        if first_name.is_visible():
            print("First name field is visible")

        # --------------------------------------------------
        # 9. MULTIPLE TABS
        # --------------------------------------------------

        # IMPORTANT:
        # Only use expect_page() when the action actually
        # opens a NEW tab/page.

        #
        # Example syntax:
        #
        # with context.expect_page() as page_info:
        #     page.get_by_text("Open").click()
        #
        # new_page = page_info.value
        #
        # print(new_page.url)

        # --------------------------------------------------
        # 3. FILE UPLOAD
        # --------------------------------------------------

        # If page contains:
        #
        # <input type="file">
        #
        # use:
        #
        # page.locator("input[type='file']").set_input_files(
        #     "C:/Users/DELL/Desktop/resume.pdf"
        # )

        # We are keeping this commented because the current
        # practice page doesn't provide an upload control
        # suitable for this test.

        # --------------------------------------------------
        # 4. FILE DOWNLOAD
        # --------------------------------------------------

        # Syntax:
        #
        # with page.expect_download() as download_info:
        #     page.get_by_text("Download").click()
        #
        # download = download_info.value
        #
        # download.save_as("report.pdf")

        # --------------------------------------------------
        # 5. DROPDOWN
        # --------------------------------------------------

        # Normal HTML <select>:
        #
        # page.locator("#country").select_option("India")
        #
        # Or:
        #
        # page.locator("#country").select_option(
        #     label="India"
        # )

        # --------------------------------------------------
        # 6. CHECKBOX
        # --------------------------------------------------

        # Syntax:
        #
        # page.locator("#terms").check()
        #
        # Uncheck:
        #
        # page.locator("#terms").uncheck()

        # --------------------------------------------------
        # 7. RADIO BUTTON
        # --------------------------------------------------

        # Syntax:
        #
        # page.locator("#male").check()

        # --------------------------------------------------
        # 8. ALERT / DIALOG
        # --------------------------------------------------

        # Accept alert:
        #
        # page.on(
        #     "dialog",
        #     lambda dialog: dialog.accept()
        # )
        #
        # Dismiss alert:
        #
        # page.on(
        #     "dialog",
        #     lambda dialog: dialog.dismiss()
        # )

        print("Practice completed")

        browser.close()