import time

from playwright.sync_api import Playwright, sync_playwright

# playwright chromium env:
# uv run playwright install chromium


def test_webauto_01(pw: Playwright):
    browser = pw.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.baidu.com")

    page.fill("#chat-textarea", value="playwright")
    page.press("#chat-textarea", key="Enter")

    page.wait_for_load_state("networkidle")
    print("result:", page.title())

    page.screenshot(path="/tmp/test/search.png", full_page=True)
    page.wait_for_load_state("networkidle")

    time.sleep(1)
    browser.close()


if __name__ == "__main__":
    with sync_playwright() as p:
        test_webauto_01(p)

    print("web auto finished")
