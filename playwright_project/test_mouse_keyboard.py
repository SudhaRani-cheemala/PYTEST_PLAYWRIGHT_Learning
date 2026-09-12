from playwright.sync_api import sync_playwright


def test_mouse_keyboard_actions():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://www.google.com")

        # 1. Click
        search_box = page.locator("textarea[name='q']")
        search_box.click()

        # 2. Type text
        search_box.fill("Playwright Python")

        # 3. Keyboard action - press Enter
        search_box.press("Enter")

        page.wait_for_load_state("domcontentloaded")

        # 4. Hover
        page.locator("body").hover()

        # 5. Double click
        page.locator("body").dblclick()

        # 6. Right click
        page.locator("body").click(button="right")

        # 7. Keyboard shortcut
        page.keyboard.press("Control+A")

        # 8. Press Escape
        page.keyboard.press("Escape")

        browser.close()




        from playwright.sync_api import sync_playwright


def test_mouse_keyboard_actions():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://www.google.com")

        # CLICK
        search = page.locator("textarea[name='q']")
        search.click()

        # FILL
        search.fill("Playwright Python")

        # PRESS ENTER
        search.press("Enter")

        page.wait_for_load_state("domcontentloaded")

        # HOVER
        page.get_by_role("link", name="Images").hover()

        # KEYBOARD SHORTCUT
        page.keyboard.press("Control+A")

        # ESCAPE
        page.keyboard.press("Escape")

        browser.close()