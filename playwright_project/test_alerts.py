from playwright.sync_api import sync_playwright


def test_alert():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/javascript_alerts")

        def handle_alert(dialog):
            print("Alert message:", dialog.message)
            dialog.accept()

        page.on("dialog", handle_alert)

        page.get_by_role(
            "button",
            name="Click for JS Alert"
        ).click()

        browser.close()