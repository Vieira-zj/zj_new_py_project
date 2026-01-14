from agentrun.sandbox import Sandbox, TemplateType
from playwright.sync_api import sync_playwright


def hello_world_help():
    print("it's a hello world demo for sandbox+playwright")


def hello_world():
    sandbox = Sandbox.create(
        template_type=TemplateType.BROWSER,
        template_name="my-template",
        sandbox_idle_timeout_seconds=300,
    )

    cdp_url = sandbox.get_cdp_url()
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(cdp_url)
        page = browser.contexts[0].pages[0]
        page.goto("https://www.example.com")
        page.screenshot(path="screenshot")
        browser.close()

    sandbox.delete()


if __name__ == "__main__":
    hello_world()
