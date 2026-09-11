from playwright.sync_api import sync_playwright,expect
def test_dropdown():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        context=browser.new_context()
        page=context.new_page()
        page.goto("https://the-internet.herokuapp.com/dropdown")
        dropdown=page.locator("#dropdown")
        dropdown.select_option(label="Option 1")
        dropdown.select_option("1")
        expect(dropdown).to_have_value("1")
        browser.close()


# | Requirement           | Playwright                        |
# | --------------------- | --------------------------------- |
# | Find dropdown         | `locator()`                       |
# | Select by value       | `select_option("1")`              |
# | Select by label       | `select_option(label="Option 2")` |
# | Verify selected value | `expect().to_have_value()`        |

# Important

# select_option() works for a normal HTML:

# <select>

# dropdown.

# Some modern applications use custom dropdowns made with <div>, <li>, etc. For those, we usually interact with them using click + locator, not select_option().
